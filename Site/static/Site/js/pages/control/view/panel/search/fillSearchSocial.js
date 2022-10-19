import {componentsData} from "../../../componentsData";
import {socialList} from "../../../../../storage/control/socialList";
import {social} from "../../../../../components/social/social";
import {makeBtnEvent} from "./makeBtnEvent";

export const fillSearchSocial = () => {
    const {viewSearch} = componentsData;
    socialList.value.forEach(el => {
        viewSearch.append(social(el));
    });
    makeBtnEvent();
};