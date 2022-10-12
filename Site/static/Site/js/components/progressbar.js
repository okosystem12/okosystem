export const progressbar = (data = {}) =>
    `<div class="progressbar">
<div class="progressbar__bar">
<div class="progressbar__value" style="width: ${data.value}%; ${data.color ? ('background-color:' + data.color) : ''}"></div>
</div>
<div>${data.title}</div>
</div>`;