import {Storage} from "./Storage";

export class StorageList extends Storage {
    clear() {
        this.value = [];
    }

    push(value) {
        this.value.push(value);
    }

    pushList(value) {
        value.forEach(el => this.push(el))
    }

    remove(key, value){
        this.value = this.value.filter(el => el[key] !== value)
    }

}