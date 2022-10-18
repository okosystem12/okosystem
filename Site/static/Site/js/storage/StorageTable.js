import {Storage} from "./Storage";

export class StorageTable extends Storage {
    constructor(value = {}) {
        super(value);
    }

    clear() {
        this.value = {};
    }

    setTable (data) {
        this.value = {
            columnsList: data.columnsList,
            renderList: data.renderList,
            patternList: data.patternList,
            patternColumnsList: data.patternColumnsList
        };
    }
}