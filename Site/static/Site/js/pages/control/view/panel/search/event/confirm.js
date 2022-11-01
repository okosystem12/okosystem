import {confirmModal} from "../../../../../../utils/modal/confirmModal";
import {confirm as setConfirm} from "../../../../../../req/control/social/confirm";
import {response} from "./response";

export const confirm = (e) => {
    confirmModal('Данная соц.сеть относится к пользователю!', () =>
        setConfirm(e.currentTarget.dataset.id, response));
};