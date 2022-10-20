import {errorPlacement} from "./errorPlacement";
import {success} from "./success";
import {highlight} from "./highlight";
import {unhighlight} from "./unhighlight";

export const init = {
    ignore: false,
    errorElement: "em",
    errorPlacement: errorPlacement,
    success: success,
    highlight: (element) => highlight(element),
    unhighlight: unhighlight
};