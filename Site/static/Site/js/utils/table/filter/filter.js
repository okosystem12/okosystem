import {action} from "./action";

export const filter = (options) => {
    if (options.filter?.length) {
        return {
            extend: 'collection',
            className: 'custom-html-collection',
            text: 'Фильтр',
            buttons: [
                ...options.filter.map(el => {
                    return {
                        ...el,
                        action: (e, dt, node, config) => {
                            el.action(e, dt, node, config, () => action(dt, options));
                        }
                    }
                }),
                '<h3></h3>',
                {
                    text: 'Сбросить',
                    action: (e, dt, node, config) => {
                        options.table.filter = {};
                        action(dt, options)
                    }
                },
            ],
        }
    }
};