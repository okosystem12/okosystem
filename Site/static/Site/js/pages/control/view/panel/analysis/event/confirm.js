import {confirmModal} from "../../../../../../utils/confirmModal";
import {componentsData} from "../../../../componentsData";
import {confirm as setConfirm} from "../../../../../../req/control/analysis/confirm";
import {response} from "./response";

export const confirm = (e) => {
    confirmModal('Материалы содержат указанное нарушение!', () => {
        // const {viewSearch} = componentsData;
        // setConfirm(e.currentTarget.dataset.id, response);
        // viewSearch.find(`.social-list__date[data-confirmed="${e.currentTarget.dataset.confirmed}"]`).html(`Подтверждено ${new Date().toLocaleString('ru')}`);
        // e.currentTarget.disabled = true
    });
};