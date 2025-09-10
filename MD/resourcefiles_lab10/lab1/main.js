function init() {
    // 1) Scene
    const scene = new THREE.Scene();

    // 2) Camera
    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );
    camera.position.z = 5;

    // 3) Renderer
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.getElementById("webgl").appendChild(renderer.domElement);

    // 4) ฟังก์ชันสร้างกล่อง
    function getBox(w, h, d, color = 0x00ff00) {
        const geometry = new THREE.BoxGeometry(w, h, d);
        const material = new THREE.MeshBasicMaterial({ color });
        const mesh = new THREE.Mesh(geometry, material);
        return mesh;
    }

    // 5) สร้างกล่องหลายกล่อง
    const boxes = [];
    for (let i = -2; i <= 2; i++) {
        const box = getBox(1, 1, 1, 0x00ff00);
        box.position.x = i * 1.5; // วางกล่องเรียงในแนวแกน X
        scene.add(box);
        boxes.push(box);
    }

    // 6) Animation loop
    function animate() {
        requestAnimationFrame(animate);

        // หมุนทุกกล่อง
        boxes.forEach((b, idx) => {
            b.rotation.x += 0.01 + idx * 0.002;
            b.rotation.y += 0.01 + idx * 0.002;
        });

        renderer.render(scene, camera);
    }

    animate();
}

init();
