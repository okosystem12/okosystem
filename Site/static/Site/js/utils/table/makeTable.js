import {settings} from "./configTable/settings";
import {columnsBtn} from "./configTable/columnsBtn";
import {buttonsExport} from "./handler/buttonsExport";
import {buttonsColvis} from "./handler/buttonsColvis";
import {colvisGroup} from "./configTable/colvisGroup";
import {prepColumnsList} from "./configTable/prepColumnsList";
import {buttonsInit} from "./handler/buttonsInit";
import {filter} from "./filter/filter";
import {fillFilterInfo} from "./filter/fillFilterInfo";

export const makeTable = (table, options = {}) => {

    const columnsBtnList = columnsBtn(options.btnList);

    const prepList = prepColumnsList(options.table);

    const visList = prepList.filter(el => !el.hide);

    fillFilterInfo(options);

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
                            dt.state.clear().destroy();
                            options.destroyCallback();
                            if('ajax' in options) dt.ajax.reload(false);
                        }
                    },
                    ...(buttonsColvis(visList)?.buttons || []),
                    ...colvisGroup(options.table),
                ]

            },
            filter(options),
            {
                text: 'Обновить',
                action: (e, dt, node, config) =>{
                    if('ajax' in options) {
                        dt.ajax.reload(false)
                    }
                    else {
                        options.destroyCallback()
                    }
                }
            }
        ]
    })
        .on('draw', () => buttonsInit(options))
        .on('responsive-display', () => buttonsInit(options))


};
