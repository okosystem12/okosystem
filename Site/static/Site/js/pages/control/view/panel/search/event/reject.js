import {confirmModal} from "../../../../../../utils/modal/confirmModal";
import {reject as setReject} from "../../../../../../req/control/social/reject";
import {response} from "./response";

export const reject = (e) => {
    confirmModal('Данная соц.сеть не относится к пользователю!', ()=>
        setReject(e.currentTarget.dataset.id, response));
};