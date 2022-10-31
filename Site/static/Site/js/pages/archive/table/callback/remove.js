import {table} from "../../../../storage/archive/table";
import {showNotificationDanger} from "../../../../utils/notification/showNotificationDanger";
import {post} from "../../../../req/archive/remove/post";
import {res} from "./res";
import {video} from "../../../../req/archive/remove/video";
import {group} from "../../../../req/archive/remove/group";
import {photo} from "../../../../req/archive/remove/photo";
import {inf} from "../../../../req/archive/remove/inf";


export const remove = (id) => {

    const row = table.value.table.row(`#${id}`).data();

    if (row) {
        switch (row.materials.type) {
            case 'post':
                post({id: row.realId}, res);
                break;
            case 'video':
                video({id: row.realId}, res);
                break;
            case 'group':
                group({id: row.realId}, res);
                break;
            case 'photo':
                photo({id: row.realId}, res);
                break;
            case 'inf':
                inf({id: row.realId}, res);
                break;
            default:
                showNotificationDanger('Ошибка определения типа записи');
                break;
        }
    }
};