import {componentsData} from "../../pages/config/place/componentsData";
import {init as initHandler} from "./handler/init";
import {countryForm as submitCountryForm} from "../submit/countryForm";

export const countryForm = () => {
    const countryNameLength = 2;
    const {countryForm} = componentsData;

    countryForm.validate({
        rules: {
            countryName: {
                required: true,
                minlength: countryNameLength,
                normalizer: $.trim
            },

        },
        messages: {
            countryName: {
                required: `Пожалуйста укажите название страны`,
                minlength: `Название страны должно содержать не менее ${countryNameLength} символов`
            },
        },
        ...initHandler,
        submitHandler: submitCountryForm
    });
};