import {settings} from "./handler/settings";
import {columnsBtn} from "./configTable/columnsBtn";
import {buttonsExport} from "./handler/buttonsExport";
import {buttonsColvis} from "./handler/buttonsColvis";
import {colvisGroup} from "./configTable/colvisGroup";
import {highlight} from "./handler/highlight";
import {prepColumnsList} from "./configTable/prepColumnsList";
import {remove} from "./event/remove";
import {edit} from "./event/edit";
import {view} from "./event/view";
import {buttonsInit} from "./handler/buttonsInit";

export const makeTable = (table, options = {}) => {

    const columnsBtnList = columnsBtn(options.btnList);

    const prepList = prepColumnsList(options.table);

    const visList = prepList.filter(el => !el.hide);

    return table.DataTable({
        ...settings,
        data: [],
        ...('ajax' in options ? {
            processing: true,
            serverSide: true,
            serverMethod: 'post',
            ajax: options.ajax
        } : {}),
        colReorder: {
            fixedColumnsLeft: options.table.columnsList.filter(el => el.fixed).length,
            fixedColumnsRight: columnsBtnList.length,
        },
        rowId: 'id',
        columns: [
            ...prepList,
            ...columnsBtnList
        ],
        buttons: [
            {
                ...buttonsExport,
            },
            {
                ...buttonsColvis(visList),
                buttons: [
                    {
                        text: 'Сбросить',
                        action: (e, dt, node, config) => {
                            options.table.table.state.clear().destroy();
                            options.destroyCallback();
                            dt.ajax.reload(false);
                        }
                    },
                    ...(buttonsColvis(visList)?.buttons || []),
                    ...colvisGroup(options.table),
                ]

            },
            {
                text: 'Обновить',
                action: (e, dt, node, config) =>
                    dt.ajax.reload(false)
            }
        ]
    })
        .on('draw', () => buttonsInit(options))
        .on('responsive-display', () => buttonsInit(options))

};
