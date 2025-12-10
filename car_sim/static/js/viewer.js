// viewer.js
// Simple Three.js 3D preview (module)
import * as THREE from "https://cdn.jsdelivr.net/npm/three@0.164/build/three.module.js";
import { GLTFLoader } from "https://cdn.jsdelivr.net/npm/three@0.164/examples/jsm/loaders/GLTFLoader.js";

let scene, camera, renderer, car, lights;
function initViewer() {
    const container = document.getElementById("view");
    if (!container) return;

    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x111111);
    camera = new THREE.PerspectiveCamera(50, container.clientWidth/container.clientHeight, 0.1, 100);
    camera.position.set(0, 1.2, 3);

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.innerHTML = "";
    container.appendChild(renderer.domElement);

    const hemi = new THREE.HemisphereLight(0xffffff, 0x444444, 1.2);
    hemi.position.set(0, 1, 0);
    scene.add(hemi);

    const dir = new THREE.DirectionalLight(0xffffff, 0.7);
    dir.position.set(5, 10, 7);
    scene.add(dir);

    const grid = new THREE.GridHelper(10, 20, 0x222222, 0x222222);
    scene.add(grid);

    const loader = new GLTFLoader();
    // Provide fallback if no model present: simple box
    loader.load("/static/models/car.glb", (gltf) => {
        car = gltf.scene;
        car.scale.set(1,1,1);
        scene.add(car);
    }, undefined, (err) => {
        // fallback simple car block
        const geometry = new THREE.BoxGeometry(1.8,0.4,0.8);
        const material = new THREE.MeshStandardMaterial({ color: 0x2b6cb0 });
        car = new THREE.Mesh(geometry, material);
        car.position.y = 0.2;
        scene.add(car);
    });

    window.addEventListener('resize', onResize);
    animate();
}

function onResize(){
    const container = document.getElementById("view");
    if(!container) return;
    camera.aspect = container.clientWidth / container.clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(container.clientWidth, container.clientHeight);
}

function animate(){
    requestAnimationFrame(animate);
    if (car) car.rotation.y += 0.003;
    if (renderer && scene && camera) renderer.render(scene, camera);
}

window.addEventListener("load", initViewer);
window.initViewer = initViewer;
