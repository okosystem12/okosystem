import {componentsData} from "../../componentsData";
import {work} from "../../../../../req/config/place/regions/work";
import {editId} from "../../../../../storage/config/place/editId";
import {placeInfo} from "../../../../app/placeInfo";
import {highlight} from "../../../../../utils/form/highlight";
import {hide} from "../../../../../utils/modal/hide";

export const submit = (form, e) => {
    e.preventDefault();
    const {regionName, regionCountry, regionModal} = componentsData;

    work({
        id: editId.value,
        country_id: regionCountry.val(),
        title: regionName.val().trim(),
    }, (msg) => {
        if (msg.successText) {
            hide(regionModal);
            placeInfo();
        }
        else {
            highlight(regionName, msg.errorHighlight);
        }
    });
};