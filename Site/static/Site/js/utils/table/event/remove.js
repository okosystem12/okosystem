import {confirmModal} from "../../confirmModal";

export const remove = (target, callback) =>
    confirmModal('Удалить запись?', () => callback(parseInt(target.dataset.id)));