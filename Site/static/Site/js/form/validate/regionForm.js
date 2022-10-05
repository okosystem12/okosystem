import {componentsData} from "../../pages/config/place/componentsData";
import {init as initHandler} from "./handler/init";
import {regionForm as submitForm} from "../submit/regionForm";

export const regionForm = () => {
    const regionNameLength = 2;
    const {regionForm} = componentsData;

    regionForm.validate({
        rules: {
            regionCountry: {
                required: true,
            },

            regionName: {
                required: true,
                minlength: regionNameLength,
                normalizer: $.trim
            },
        },
        messages: {
            regionCountry: {
                required: `Пожалуйста выберите название страны из представленного списска`,
            },
            regionName: {
                required: `Пожалуйста укажите название региона`,
                minlength: `Название региона должно содержать не менее ${regionNameLength} символов`
            },
        },
        ...initHandler,
        submitHandler: submitForm
    });
};