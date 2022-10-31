import {componentsData} from "../../../componentsData";
import {corruptList} from "../../../../../storage/control/corruptList";

export const fillAnalysis = (data = null) => {
    if (data) {
        const {viewAnalysis} = componentsData;
        viewAnalysis.html('');

        corruptList.value.filter(el => el.controlUser_id === data.id).forEach(el => {
            // viewAnalysis.append(social(el));
            console.log(el);
        });
        // makeBtnEvent();
    }
};