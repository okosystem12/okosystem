const exportOptions = {
    orthogonal: 'export',
    columns: 'th:not(.noExport)'
};

export const buttonsExport =
    {
        extend: 'collection',
        className: 'custom-html-collection',
        text: 'Экспорт',
        buttons: [
            {
                extend: 'copyHtml5',
                exportOptions
            },
            {
                extend: 'excelHtml5',
                exportOptions
            },
            {
                extend: 'csvHtml5',
                exportOptions
            },
            {
                extend: 'pdfHtml5',
                exportOptions
            },
            {
                extend: 'print',
                exportOptions
            }
        ]
    }
;