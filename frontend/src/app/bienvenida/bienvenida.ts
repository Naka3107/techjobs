import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-bienvenida',
  imports: [RouterLink],
  templateUrl: './bienvenida.html',
  styleUrl: './bienvenida.scss'
})
export class Bienvenida implements OnInit, OnDestroy {
  private animationId: number = 0;

  ngOnInit(): void {
    const canvas = document.getElementById('matrix-canvas') as HTMLCanvasElement;
    const ctx = canvas.getContext('2d')!;

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789<>{}[]();=+-*/';
    const fontSize = 20;
    const columns = Math.floor(canvas.width / fontSize);
    const drops: number[] = Array(columns).fill(0).map(() => Math.floor(Math.random() * -100));
    const activas: boolean[] = Array(columns).fill(false).map(() => Math.random() > 0.6);
    const cooldown: number[] = Array(columns).fill(0); // frames de espera antes de reactivarse

    const draw = () => {
      ctx.fillStyle = 'rgba(13, 13, 13, 0.3)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.fillStyle = 'rgba(255, 255, 255, 0.12)';
      ctx.font = `${fontSize}px monospace`;

      for (let i = 0; i < drops.length; i++) {
        // Si está en cooldown, descuenta y espera
        if (cooldown[i] > 0) {
          cooldown[i]--;
          continue;
        }

        // Si no está activa, actívala con probabilidad baja por frame
        if (!activas[i]) {
          if (Math.random() > 0.995) activas[i] = true;
          continue;
        }

        const char = chars[Math.floor(Math.random() * chars.length)];
        ctx.fillText(char, i * fontSize, drops[i] * fontSize);
        drops[i]++;

        if (drops[i] * fontSize > canvas.height) {
          drops[i] = 0;
          activas[i] = false;
          cooldown[i] = Math.floor(Math.random() * 200) + 50; // espera entre 50 y 250 frames
        }
      }

      this.animationId = setTimeout(draw, 32) as unknown as number;
    };
    draw();

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };
    resize();
    window.addEventListener('resize', resize);
  }

  ngOnDestroy(): void {
    clearTimeout(this.animationId);
  }
}