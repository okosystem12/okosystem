import {dataTablesRu} from '../../../../vendor/dataTables/dataTables.ru.js'

export const settings = {
    dom: 'lBfrtip',
    destroy: true,
    autoWidth: true,
    fixedHeader: true,
    resizeColumn: true,
    responsive: true,
    colReorder: true,
    stateSave: true,
    language: dataTablesRu,
    search: {
        return: true,
    },
    lengthMenu: [
        [10, 25, 50, 100],
        ['10', '25', '50', '100']
    ],
};