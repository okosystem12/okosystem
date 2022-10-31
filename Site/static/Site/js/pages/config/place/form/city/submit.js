import {componentsData} from "../../componentsData";
import {work} from "../../../../../req/config/place/city/work";
import {editId} from "../../../../../storage/config/place/editId";
import {highlight} from "../../../../../utils/form/highlight";
import {idToNull} from "../../../../../utils/idToNull";
import {close} from "./close";

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
            close();
        }
        else {
            highlight(cityName, msg.errorHighlight);
        }
    });
};