import {confirmModal} from "../../../../../../utils/modal/confirmModal";
import {reject as postReject} from "../../../../../../req/control/analysis/post/reject";
import {reject as videoReject} from "../../../../../../req/control/analysis/video/reject";
import {reject as groupReject} from "../../../../../../req/control/analysis/group/reject";
import {reject as photoReject} from "../../../../../../req/control/analysis/photo/reject";
import {reject as infReject} from "../../../../../../req/control/analysis/inf/reject";
import {response} from "./response";
import {showNotificationDanger} from "../../../../../../utils/notification/showNotificationDanger";

export const reject = (e) => {
    confirmModal('Материалы не содержат указанного нарушения?', () => {
        switch (e.currentTarget.dataset.type) {
            case 'post':
                postReject(e.currentTarget.dataset.id, response);
                break;
            case 'video':
                videoReject(e.currentTarget.dataset.id, response);
                break;
            case 'group':
                groupReject(e.currentTarget.dataset.id, response);
                break;
            case 'photo':
                photoReject(e.currentTarget.dataset.id, response);
                break;
            case 'inf':
                infReject(e.currentTarget.dataset.id, response);
                break;
            default:
                showNotificationDanger('Ошибка определения типа записи');
                break;
        }
    });
};