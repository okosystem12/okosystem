import {componentsData} from "../../../componentsData";
import {socialList} from "../../../../../storage/control/socialList";
import {social} from "../../../../../components/social/social";
import {makeBtnEvent} from "./makeBtnEvent";

export const fillSearchSocial = (data = null) => {
    if (data) {
        const {viewSearch, socialCount, socialWait} = componentsData;
        viewSearch.html('');
        let count = 0;
        let wait = 0;

        socialList.value.filter(el => el.controlUser_id === data.id).forEach(el => {
            viewSearch.append(social(el));

            if (el.confirmedAt) {
                count++;
            }
            else {
                wait++;
            }
        });
        makeBtnEvent();

        if(count){
            socialCount.html(count).show();
        }

        if(wait){
            socialWait.html(wait).show();
        }
    }
};