import {countryForm} from "../../../../form/validate/countryForm";
import {regionForm} from "../../../../form/validate/regionForm";
import {cityForm} from "../../../../form/validate/cityForm";

export const validate = () => {
  countryForm();
  regionForm();
  cityForm();
};