import {highlight} from "./highlight";
import {view} from "../event/view";
import {edit} from "../event/edit";
import {remove} from "../event/remove";

export const buttonsInit = (options = {}) => {
    highlight(options.table.table);

    $('.view-table-btn')
        .off('click')
        .on('click', (e) => {
            e.preventDefault();
            view(e.currentTarget, options.viewCallback);
        });

    $('.edit-table-btn')
        .off('click')
        .on('click', (e) => {
            e.preventDefault();
            edit(e.currentTarget, options.editCallback);
        });

    $('.remove-table-btn')
        .off('click')
        .on('click', (e) => {
            e.preventDefault();
            remove(e.currentTarget, options.removeCallback);
        });
};