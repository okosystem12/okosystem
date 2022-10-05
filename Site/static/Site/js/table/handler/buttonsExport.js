export const buttonsExport =
    {
        extend: 'collection',
        className: 'custom-html-collection',
        text: 'Экспорт',
        buttons: [{
                extend: 'copyHtml5',
                exportOptions: { orthogonal: 'export' }
            },
            {
                extend: 'excelHtml5',
                exportOptions: { orthogonal: 'export' }
            },
            {
                extend: 'csvHtml5',
                exportOptions: { orthogonal: 'export' }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: { orthogonal: 'export' }
            },
            {
                extend: 'print',
                exportOptions: { orthogonal: 'export' }
            }],
    }
;