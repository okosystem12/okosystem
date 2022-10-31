import {confirmModal} from "../../../../../../utils/confirmModal";
import {componentsData} from "../../../../componentsData";
import {reject as setReject} from "../../../../../../req/control/analysis/reject";
import {response} from "./response";

export const reject = (e) => {
    confirmModal('Материалы не содержат указанного нарушения?', ()=>{
        // const {viewSearch} = componentsData;
        // setReject(e.currentTarget.dataset.id, response);
        // viewSearch.find(`.social-list[data-social="${e.currentTarget.dataset.social}"]`).remove();
    });
};