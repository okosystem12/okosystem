import {componentsData} from "../../componentsData";
import {init as initHandler} from "../../../../../utils/form/init";
import {submit} from "./submit";

export const validate = () => {
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
        submitHandler: submit
    });
};