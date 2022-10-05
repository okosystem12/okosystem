import {confirmModal} from "../../utils/confirmModal";

export const remove = (target, callback) =>
    confirmModal('Удалить запись?', () => callback(parseInt(target.dataset.id)));