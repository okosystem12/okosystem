export const columnsBtn = (btnList = []) => [
    {
        data: 'id',
        title: '',
        always: true,
        searchable: false,
        orderable: false,
        className: 'noVis noExport',
        render: function (data, type, row, meta) {
            return `<div class="table-btn-list">
${btnList.indexOf(`view`) !== -1 ? `<a href="#" data-id="${data}" class="text-muted view-table-btn" title="Открыть карточку"><span class="glyphicon glyphicon-list-alt"></span></a>` : ''}
${btnList.indexOf(`edit`) !== -1 ? `<a href="#" data-id="${data}" class="edit-table-btn" title="Редактировать"><span class="glyphicon glyphicon-pencil"></span></a>` : ''}
${btnList.indexOf(`remove`) !== -1 ? `<a href="#" data-id="${data}"  class="text-danger remove-table-btn" title="Удалить"><span class="glyphicon glyphicon-trash"></span></a>` : ''}
</div>`;
        },
    },

];