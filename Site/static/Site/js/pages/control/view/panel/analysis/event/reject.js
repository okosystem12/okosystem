import {confirmModal} from "../../../../../../utils/confirmModal";
import {reject as setReject} from "../../../../../../req/control/analysis/reject";
import {response} from "./response";

export const reject = (e) => {
    confirmModal('Материалы не содержат указанного нарушения?', () =>
        setReject(e.currentTarget.dataset.id, response));
};