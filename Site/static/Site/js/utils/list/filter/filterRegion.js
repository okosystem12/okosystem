import {regionsList} from "../../../storage/app/regionsList";

export const filterRegion = (country = null) =>
    regionsList.value.filter(el => country ? el.country_id === country : true);