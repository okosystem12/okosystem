export const filter = (options) => {
    if(options.filter?.length) {
        return {
            extend: 'collection',
            className: 'custom-html-collection',
            text: 'Фильтр',
            buttons: [
                {
                    text: 'Сбросить',
                    action: (e, dt, node, config) => {
                        dt.state.clear().destroy();
                        options.destroyCallback();
                        if ('ajax' in options) {
                            dt.ajax.url(options.ajax.url);
                            dt.ajax.reload(false);
                        }
                    }
                },
                ...options.filter,
            ],
        }
    }
};