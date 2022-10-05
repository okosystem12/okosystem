export class Storage {
    constructor(value = []) {
        this.clear();
        this.value = value;
    }

    get value(){
        return this._value;
    }

    set value(value){
        this._value = value;
    }

    clear(){
        this.value = null;
    }
}