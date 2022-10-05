import {dataTablesRu} from '../../../vendor/dataTables/dataTables.ru.js'

export const settings = {
    dom: 'lBfrtip',
    destroy : true,
    fixedHeader: true,
    responsive: true,
    colReorder: true,
    stateSave: true,
    language: dataTablesRu,
    lengthMenu: [
        [10, 25, 50,100, -1],
        ['10', '25', '50', '100', 'Все записи']
    ],
};