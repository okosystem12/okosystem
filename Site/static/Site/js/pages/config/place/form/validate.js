import {validate as countryValidate} from "./country/validate";
import {validate as regionValidate} from "./region/validate";
import {validate as cityValidate} from "./city/validate";

export const validate = () => {
  countryValidate();
  regionValidate();
  cityValidate();
};