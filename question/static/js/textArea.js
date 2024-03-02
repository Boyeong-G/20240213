function resize(obj) {
    if (obj.style.height >= 15)
        obj.style.height = '1px';
    obj.style.height = (obj.scrollHeight) + 'px';
}