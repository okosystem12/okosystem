import {user} from "../../storage/user";
import {componentsData} from "./componentsData";

export const setName = () => {
    const {userInfo} = componentsData;

    const prefix = 'Добро пожаловать, ';
    let name = '';

    if (user.value.first_name || user.value.last_name) {
        if(user.value.first_name && user.value.last_name){
             name = `${user.value.last_name} ${user.value.first_name}`;
        }
        else if(user.value.first_name){
             name = user.value.first_name;
        }
        else if(user.value.last_name){
             name = user.value.last_name;
        }
    }
    else {
       name = user.value.username;
    }
     userInfo.html(`${prefix} ${name}`);
};