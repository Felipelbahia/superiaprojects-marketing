// Centralized Catalog Application (Zero-Sync Runtime Engine)
// Single Source of Truth: 0 Padrões/.agent/catalog-app.js
if (window.__CATALOG_APP_INITIALIZED__) {
  console.log("ℹ️ Catalog App já inicializado pela instância mestre central.");
} else {
  window.__CATALOG_APP_INITIALIZED__ = true;

  // Inicialização e consolidação das bases de dados
  let items = [];
  const sourcesLoaded = [];

  // 1. Tenta carregar dados do Projeto Local
    if (window.CATALOG_LOCAL && window.CATALOG_LOCAL.items && window.CATALOG_LOCAL.items.length > 0) {
      items = items.concat(window.CATALOG_LOCAL.items);
      sourcesLoaded.push(`Local (${window.CATALOG_LOCAL.items.length})`);
      document.getElementById('pillLocal').style.display = 'inline-block';
    }

    // 2. Tenta carregar dados de 0 Padrões
    if (window.CATALOG_0_PADROES && window.CATALOG_0_PADROES.items && window.CATALOG_0_PADROES.items.length > 0) {
      if (!window.CATALOG_LOCAL || window.CATALOG_LOCAL.source !== "0 Padrões") {
        items = items.concat(window.CATALOG_0_PADROES.items);
        sourcesLoaded.push(`0 Padrões (${window.CATALOG_0_PADROES.items.length})`);
      }
    }

    // 3. Tenta carregar dados de 0 Mkt
    if (window.CATALOG_0_MKT && window.CATALOG_0_MKT.items && window.CATALOG_0_MKT.items.length > 0) {
      if (!window.CATALOG_LOCAL || window.CATALOG_LOCAL.source !== "0 Mkt") {
        items = items.concat(window.CATALOG_0_MKT.items);
        sourcesLoaded.push(`0 Mkt (${window.CATALOG_0_MKT.items.length})`);
      }
    }

    // 4. Fallback: Se nenhum script externo carregou, usa os dados embutidos
    if (items.length === 0 && window.EMBEDDED_CATALOG_DATA) {
      items = window.EMBEDDED_CATALOG_DATA;
      sourcesLoaded.push("Dados Embutidos");
    }

    document.getElementById('sourcesActiveInfo').textContent = sourcesLoaded.join(' + ');

    // Filtros de Estado
    let activeSourceFilter = 'all';
    let searchQuery = '';
    let currentView = 'grid';
    let currentSelectedItem = null;

    // Categorias selecionadas (Seleção Múltipla)
    let selectedCategories = new Set(items.map(i => i.category));
    let allAvailableCategories = [];

    function updateSelectedCatsCounter() {
      const counterEl = document.getElementById('selectedCatsCount');
      if (!counterEl) return;
      if (selectedCategories.size === 0) {
        counterEl.textContent = '0 selecionadas';
        counterEl.style.color = 'var(--text-dim)';
      } else if (selectedCategories.size === allAvailableCategories.length) {
        counterEl.textContent = 'Todas selecionadas';
        counterEl.style.color = 'var(--accent)';
      } else {
        counterEl.textContent = `${selectedCategories.size} de ${allAvailableCategories.length} selecionadas`;
        counterEl.style.color = 'var(--primary)';
      }
    }

    // Constrói as linhas de categorias para cada projeto
    function buildCategoriesPanel() {
      const container = document.getElementById('categoriesRows');
      if (!container) return;
      container.innerHTML = '';

      // Agrupa itens por fonte
      const sourcesMap = {
        'Projeto Local': [],
        '0 Padrões': [],
        '0 Mkt': []
      };

      items.forEach(it => {
        if (!sourcesMap[it.source]) sourcesMap[it.source] = [];
        sourcesMap[it.source].push(it);
      });

      // Determina quais fontes exibir de acordo com activeSourceFilter
      let visibleSources = [];
      if (activeSourceFilter === 'local') visibleSources = ['Projeto Local'];
      else if (activeSourceFilter === 'padroes') visibleSources = ['0 Padrões'];
      else if (activeSourceFilter === 'mkt') visibleSources = ['0 Mkt'];
      else visibleSources = ['Projeto Local', '0 Padrões', '0 Mkt'];

      allAvailableCategories = [];

      visibleSources.forEach(src => {
        const srcItems = sourcesMap[src] || [];
        if (srcItems.length === 0) return;

        // Contagem de categorias nesta fonte
        const catCounts = {};
        srcItems.forEach(i => {
          catCounts[i.category] = (catCounts[i.category] || 0) + 1;
        });

        const cats = Object.keys(catCounts).sort();
        cats.forEach(c => {
          if (!allAvailableCategories.includes(c)) allAvailableCategories.push(c);
        });

        const row = document.createElement('div');
        row.className = 'cat-project-row';

        let srcBadgeClass = 'badge-src-padroes';
        if (src === '0 Mkt') srcBadgeClass = 'badge-src-mkt';
        if (src === 'Projeto Local') srcBadgeClass = 'badge-src-local';

        const labelWrap = document.createElement('div');
        labelWrap.className = 'cat-source-label';
        labelWrap.innerHTML = `<span class="badge ${srcBadgeClass}">${src}</span>`;
        row.appendChild(labelWrap);

        const chipsList = document.createElement('div');
        chipsList.className = 'cat-chips-list';

        cats.forEach(c => {
          const btn = document.createElement('button');
          btn.type = 'button';
          const isSelected = selectedCategories.has(c);
          btn.className = `cat-chip ${isSelected ? 'active' : ''}`;
          btn.dataset.category = c;
          btn.dataset.source = src;
          btn.innerHTML = `${c} <span class="cat-count">(${catCounts[c]})</span>`;
          btn.onclick = () => toggleCategory(c);
          chipsList.appendChild(btn);
        });

        row.appendChild(chipsList);
        container.appendChild(row);
      });

      updateSelectedCatsCounter();
    }

    function toggleCategory(catName) {
      if (selectedCategories.has(catName)) {
        selectedCategories.delete(catName);
      } else {
        selectedCategories.add(catName);
      }
      document.querySelectorAll(`.cat-chip[data-category="${catName}"]`).forEach(el => {
        if (selectedCategories.has(catName)) el.classList.add('active');
        else el.classList.remove('active');
      });
      updateSelectedCatsCounter();
      render();
    }

    function selectAllCategories(e) {
      if (e) e.stopPropagation();
      allAvailableCategories.forEach(c => selectedCategories.add(c));
      document.querySelectorAll('.cat-chip').forEach(el => el.classList.add('active'));
      updateSelectedCatsCounter();
      render();
    }

    function clearAllCategories(e) {
      if (e) e.stopPropagation();
      selectedCategories.clear();
      document.querySelectorAll('.cat-chip').forEach(el => el.classList.remove('active'));
      updateSelectedCatsCounter();
      render();
    }

    document.getElementById('btnSelectAllCats').onclick = (e) => selectAllCategories(e);
    document.getElementById('btnClearAllCats').onclick = (e) => clearAllCategories(e);

    buildCategoriesPanel();

    function normalizeStr(s) {
      return (s || '').normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase().replace(/[-_]/g, " ");
    }

    function getSelectedKinds() {
      const kinds = [];
      document.querySelectorAll('.checkbutton input:checked').forEach(cb => {
        kinds.push(cb.value);
      });
      return kinds;
    }

    function filterItems() {
      const q = normalizeStr(searchQuery);
      const qTerms = q.split(/\s+/).filter(Boolean);
      const selectedKinds = getSelectedKinds();

      return items.filter(it => {
        // Filtro de Origem
        if (activeSourceFilter === 'local' && it.source !== 'Projeto Local') return false;
        if (activeSourceFilter === 'padroes' && it.source !== '0 Padrões') return false;
        if (activeSourceFilter === 'mkt' && it.source !== '0 Mkt') return false;

        // Filtro de Tipo (Checkbuttons múltiplos)
        if (!selectedKinds.includes(it.kind)) return false;

        // Filtro de Categoria (Multi-seleção de categorias por chips)
        if (selectedCategories.size === 0) return false;
        if (!selectedCategories.has(it.category)) return false;

        // Busca por múltiplos termos
        if (qTerms.length > 0) {
          const searchable = normalizeStr(`${it.name} ${it.desc} ${it.category} ${it.subcategory} ${it.kind} ${it.source}`);
          for (let term of qTerms) {
            if (!searchable.includes(term)) return false;
          }
        }

        return true;
      });
    }

    function render() {
      const filtered = filterItems();
      document.getElementById('resultsCount').textContent = `Exibindo ${filtered.length} de ${items.length} recursos`;

      // Render Grid
      const grid = document.getElementById('gridView');
      grid.innerHTML = '';
      filtered.forEach(it => {
        const card = document.createElement('div');
        card.className = 'card';
        card.onclick = () => openModal(it);

        let kindClass = 'badge-skill';
        if (it.kind === 'Workflow') kindClass = 'badge-wf';
        if (it.kind === 'Agent') kindClass = 'badge-agent';

        let srcClass = 'badge-src-padroes';
        if (it.source === '0 Mkt') srcClass = 'badge-src-mkt';
        if (it.source === 'Projeto Local') srcClass = 'badge-src-local';

        card.innerHTML = `
          <div class="card-header">
            <div class="card-title">${it.name}</div>
            <div class="badges">
              <span class="badge ${kindClass}">${it.kind}</span>
              <span class="badge ${srcClass}">${it.source}</span>
            </div>
          </div>
          <div class="card-category">📁 ${it.category} › ${it.subcategory}</div>
          <div class="card-desc">${it.desc}</div>
          <div class="card-footer">
            <span>${it.files && it.files.length > 0 ? '📂 ' + it.files.length + ' refs' : ''}</span>
            <span class="click-hint">Ver Detalhes &rarr;</span>
          </div>
        `;
        grid.appendChild(card);
      });

      // Render Table com colunas separadas para Categoria e Subcategoria
      const tbody = document.getElementById('tableBody');
      tbody.innerHTML = '';
      filtered.forEach(it => {
        const tr = document.createElement('tr');
        tr.onclick = () => openModal(it);

        let kindClass = 'badge-skill';
        if (it.kind === 'Workflow') kindClass = 'badge-wf';
        if (it.kind === 'Agent') kindClass = 'badge-agent';

        let srcClass = 'badge-src-padroes';
        if (it.source === '0 Mkt') srcClass = 'badge-src-mkt';
        if (it.source === 'Projeto Local') srcClass = 'badge-src-local';

        tr.innerHTML = `
          <td class="td-name">${it.name}</td>
          <td><span class="badge ${kindClass}">${it.kind}</span></td>
          <td><span class="badge ${srcClass}">${it.source}</span></td>
          <td style="font-weight:600; color:var(--text);">${it.category}</td>
          <td>${it.subcategory}</td>
          <td>${it.desc}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    // Modal Central de Detalhes da Skill
    const modalOverlay = document.getElementById('modalOverlay');
    const itemModal = document.getElementById('itemModal');
    const modalClose = document.getElementById('modalClose');

    function openModal(item) {
      currentSelectedItem = item;
      document.getElementById('modalTitle').textContent = item.name;
      document.getElementById('modalCategory').textContent = item.category;
      document.getElementById('modalSubcategory').textContent = item.subcategory;
      document.getElementById('modalDesc').textContent = item.desc;
      document.getElementById('modalPath').textContent = item.abs_path || item.path;
      document.getElementById('modalContent').textContent = item.content || "(Sem conteúdo adicional registrado)";

      // Badges
      const badgesContainer = document.getElementById('modalBadges');
      badgesContainer.innerHTML = '';
      const bKind = document.createElement('span');
      bKind.className = `badge badge-${item.kind.toLowerCase()}`;
      bKind.textContent = item.kind;
      badgesContainer.appendChild(bKind);

      const bSrc = document.createElement('span');
      let srcClass = item.source === '0 Mkt' ? 'badge-src-mkt' : (item.source === 'Projeto Local' ? 'badge-src-local' : 'badge-src-padroes');
      bSrc.className = `badge ${srcClass}`;
      bSrc.textContent = item.source;
      badgesContainer.appendChild(bSrc);

      // Files Section (Dropdown / Collapsible)
      const filesDetails = document.getElementById('modalFilesDetails');
      const filesList = document.getElementById('modalFilesList');
      filesList.innerHTML = '';

      if (item.files && item.files.length > 0) {
        filesDetails.style.display = 'block';
        filesDetails.open = true;
        document.getElementById('filesCount').textContent = item.files.length;
        item.files.forEach(f => {
          const li = document.createElement('li');
          if (f.content && f.content.trim()) {
            const det = document.createElement('details');
            det.className = 'ref-file-collapsible';

            const sum = document.createElement('summary');
            sum.className = 'ref-file-header';
            sum.innerHTML = `
              <div class="ref-file-info">
                <span>📄</span>
                <span>${f.rel_path}</span>
              </div>
              <div class="ref-actions">
                <a class="ref-open-link" href="file://${f.abs_path}" target="_blank" title="Abrir arquivo externo" onclick="event.stopPropagation()">↗ Abrir</a>
                <span class="collapsible-chevron">▾</span>
              </div>
            `;

            const body = document.createElement('div');
            body.className = 'ref-file-body';

            const box = document.createElement('div');
            box.className = 'content-box ref-content-box';
            box.textContent = f.content;

            body.appendChild(box);
            det.appendChild(sum);
            det.appendChild(body);
            li.appendChild(det);
          } else {
            li.innerHTML = `<a class="file-link" href="file://${f.abs_path}" target="_blank">📄 ${f.rel_path} <span style="margin-left:auto; opacity:0.6;">↗</span></a>`;
          }
          filesList.appendChild(li);
        });
      } else {
        filesDetails.style.display = 'none';
      }

      // Content Section (Dropdown / Collapsible)
      const contentDetails = document.getElementById('modalContentDetails');
      contentDetails.open = true;
      document.getElementById('modalContentLabel').textContent = item.kind === 'Workflow' ? 'WORKFLOW.md' : (item.kind === 'Agent' ? 'AGENT.md' : 'SKILL.md');

      modalOverlay.classList.add('open');
      document.body.style.overflow = 'hidden';
      itemModal.querySelector('.modal-body').scrollTop = 0;
    }

    function closeModal() {
      modalOverlay.classList.remove('open');
      document.body.style.overflow = '';
    }

    modalClose.onclick = closeModal;
    modalOverlay.onclick = (e) => {
      if (e.target === modalOverlay) closeModal();
    };
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
    });

    // Ações de Cópia
    document.getElementById('btnCopyPath').onclick = () => {
      if (currentSelectedItem) {
        navigator.clipboard.writeText(currentSelectedItem.abs_path || currentSelectedItem.path);
        alert('Caminho copiado com sucesso!');
      }
    };

    document.getElementById('btnCopyUsage').onclick = () => {
      if (currentSelectedItem) {
        let usage = '';
        if (currentSelectedItem.kind === 'Workflow') usage = currentSelectedItem.name;
        else if (currentSelectedItem.kind === 'Agent') usage = currentSelectedItem.name;
        else usage = `ln -s "${currentSelectedItem.abs_path}" .claude/skills/${currentSelectedItem.name}`;
        navigator.clipboard.writeText(usage);
        alert(`Invocação copiada: ${usage}`);
      }
    };

    // Eventos de Busca e Filtros
    document.getElementById('searchInput').addEventListener('input', (e) => {
      searchQuery = e.target.value;
      render();
    });

    document.getElementById('categorySelect').addEventListener('change', (e) => {
      activeCatFilter = e.target.value;
      render();
    });

    // Checkbuttons de Tipo (Skill, Workflow, Agent)
    document.querySelectorAll('.checkbutton input[type="checkbox"]').forEach(cb => {
      cb.addEventListener('change', (e) => {
        const parentLabel = e.target.closest('.checkbutton');
        if (e.target.checked) {
          parentLabel.classList.add('active');
        } else {
          parentLabel.classList.remove('active');
        }
        render();
      });
    });

    // Pills de filtro de Origem
    document.querySelectorAll('.pill').forEach(pill => {
      pill.addEventListener('click', () => {
        if (pill.dataset.filter === 'all') {
          activeSourceFilter = 'all';
          document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          document.querySelectorAll('.checkbutton input[type="checkbox"]').forEach(cb => {
            cb.checked = true;
            cb.closest('.checkbutton').classList.add('active');
          });
        } else if (pill.dataset.source) {
          document.querySelectorAll('[data-source]').forEach(p => p.classList.remove('active'));
          document.querySelector('[data-filter="all"]').classList.remove('active');
          if (activeSourceFilter === pill.dataset.source) {
            activeSourceFilter = 'all';
            document.querySelector('[data-filter="all"]').classList.add('active');
          } else {
            activeSourceFilter = pill.dataset.source;
            pill.classList.add('active');
          }
        }
        buildCategoriesPanel();
        render();
      });
    });

    // Alternar Visualização Grid / Tabela
    const viewToggle = document.getElementById('viewToggle');
    viewToggle.onclick = () => {
      const grid = document.getElementById('gridView');
      const table = document.getElementById('tableView');
      if (currentView === 'grid') {
        grid.style.display = 'none';
        table.style.display = 'block';
        viewToggle.textContent = '🔲 Grid';
        currentView = 'table';
      } else {
        grid.style.display = 'grid';
        table.style.display = 'none';
        viewToggle.textContent = '📋 Tabela';
        currentView = 'grid';
      }
    };

    // Alternar Tema Claro / Escuro com persistência
    const themeToggle = document.getElementById('themeToggle');
    function applyTheme(isLight) {
      if (isLight) {
        document.body.classList.add('light');
        localStorage.setItem('catalog_theme', 'light');
        themeToggle.textContent = '🌙 Escuro';
      } else {
        document.body.classList.remove('light');
        localStorage.setItem('catalog_theme', 'dark');
        themeToggle.textContent = '☀️ Claro';
      }
    }

    const savedTheme = localStorage.getItem('catalog_theme');
    if (savedTheme === 'light') {
      applyTheme(true);
    } else if (savedTheme === 'dark') {
      applyTheme(false);
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
      applyTheme(true);
    } else {
      applyTheme(false);
    }

    // Exposição global segura de handlers para inline onclicks
    window.selectAllCategories = selectAllCategories;
    window.clearAllCategories = clearAllCategories;
    window.toggleCategory = toggleCategory;
    window.openModal = openModal;
    window.closeModal = closeModal;

    // Render Inicial
    render();
}