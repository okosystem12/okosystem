import {confirmModal} from "../../../../../../utils/modal/confirmModal";
import {confirm as postConfirm} from "../../../../../../req/control/analysis/post/confirm";
import {confirm as videoConfirm} from "../../../../../../req/control/analysis/video/confirm";
import {confirm as groupConfirm} from "../../../../../../req/control/analysis/group/confirm";
import {confirm as photoConfirm} from "../../../../../../req/control/analysis/photo/confirm";
import {confirm as infConfirm} from "../../../../../../req/control/analysis/inf/confirm";
import {response} from "./response";
import {showNotificationDanger} from "../../../../../../utils/notification/showNotificationDanger";

export const confirm = (e) => {
    confirmModal('Материалы содержат указанное нарушение!', () => {
        switch (e.currentTarget.dataset.type) {
            case 'post':
                postConfirm(e.currentTarget.dataset.id, response);
                break;
            case 'video':
                videoConfirm(e.currentTarget.dataset.id, response);
                break;
            case 'group':
                groupConfirm(e.currentTarget.dataset.id, response);
                break;
            case 'photo':
                photoConfirm(e.currentTarget.dataset.id, response);
                break;
            case 'inf':
                infConfirm(e.currentTarget.dataset.id, response);
                break;
            default:
                showNotificationDanger('Ошибка определения типа записи');
                break;
        }
    });
};