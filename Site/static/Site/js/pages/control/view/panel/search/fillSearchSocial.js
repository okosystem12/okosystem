import {componentsData} from "../../../componentsData";
import {socialList} from "../../../../../storage/control/socialList";
import {social} from "../../../../../components/social/social";
import {makeBtnEvent} from "./makeBtnEvent";

export const fillSearchSocial = (data = null) => {
    if(data) {
        const {viewSearch} = componentsData;
        viewSearch.html('');

        socialList.value.filter(el => el.controlUser_id === data.id).forEach(el => {
            viewSearch.append(social(el));
        });
        makeBtnEvent();
    }
};