import {componentsData} from "../../componentsData";
import {work} from "../../../../../req/config/place/city/work";
import {editId} from "../../../../../storage/config/place/editId";
import {placeInfo} from "../../../../app/placeInfo";
import {highlight} from "../../../../../utils/form/highlight";
import {idToNull} from "../../../../../utils/idToNull";
import {hide} from "../../../../../utils/modal/hide";

export const submit = (form, e) => {
    e.preventDefault();
    const {cityName, cityRegion, cityCountry, cityModal} = componentsData;

    work({
        id: editId.value,
        region_id: idToNull(cityRegion.val()),
        country_id: idToNull(cityCountry.val()),
        title: cityName.val().trim(),
    }, (msg) => {
        if (msg.successText) {
            placeInfo();
            hide(cityModal);
        }
        else {
            highlight(cityName, msg.errorHighlight);
        }
    });
};