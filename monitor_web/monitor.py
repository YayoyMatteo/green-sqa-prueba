def mostrar_mensaje(mensaje):
    script = f"""
    const msg = document.createElement('div');
    msg.textContent = `{mensaje}`;
    msg.style.position = 'fixed';
    msg.style.top = '10px';
    msg.style.left = '50%';
    msg.style.transform = 'translateX(-50%)';
    msg.style.backgroundColor = '#222';
    msg.style.color = '#fff';
    msg.style.padding = '10px 20px';
    msg.style.borderRadius = '8px';
    msg.style.fontSize = '16px';
    msg.style.zIndex = 9999;
    msg.style.boxShadow = '0 4px 8px rgba(0,0,0,0.2)';
    document.body.appendChild(msg);
    setTimeout(() => msg.remove(), 3500);
    """
    try:
        globals()['driver'].execute_script(script)
    except Exception:
        pass

