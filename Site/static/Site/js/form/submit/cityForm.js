import {componentsData} from "../../pages/config/place/componentsData";
import {work} from "../../req/config/place/city/work";
import {editId} from "../../storage/config/place/editId";
import {placeInfo} from "../../pages/app/placeInfo";
import {highlight} from "../validate/handler/highlight";

export const cityForm = (form, e) => {
    e.preventDefault();
    const {cityName, cityRegion, cityCountry} = componentsData;

    work({
        id: editId.value,
        region_id: cityRegion.val(),
        country_id: cityCountry.val(),
        title: cityName.val().trim(),
    }, (msg) => {
        if (msg.successText) {
            $.fancybox.close();
            placeInfo();
        }
        else {
            highlight(cityName);
        }
    });
};