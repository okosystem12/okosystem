export class Storage {
    constructor(value = null) {
        this.value = value;
    }

    get value() {
        return this._value;
    }

    set value(value) {
        this._value = value;
    }

    clear() {
        this.value = null;
    }
}