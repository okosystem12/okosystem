import {confirmModal} from "../../../../../../utils/confirmModal";
import {componentsData} from "../../../../componentsData";
import {reject as setReject} from "../../../../../../req/control/social/reject";
import {response} from "./response";

export const reject = (e) => {
    confirmModal('Данная соц.сеть не относится к пользователю!', ()=>{
        const {viewSearch} = componentsData;
        setReject(e.currentTarget.dataset.id, response);
        viewSearch.find(`.social-list[data-social="${e.currentTarget.dataset.social}"]`).remove();
    });
};