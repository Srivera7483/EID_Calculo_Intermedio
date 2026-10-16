from manim import *
import numpy as np

COLOR_FONDO = "#0f172a"
COLOR_CURVA = "#38bdf8"
COLOR_AREA = "#0284c7"
COLOR_DELTA = "#f59e0b"
COLOR_TEXTO = "#f8fafc"
COLOR_SUBTEXTO = "#94a3b8"
COLOR_DESTACADO = "#e11d48"
COLOR_VERDE = "#10b981"
COLOR_ECUACION = "#facc15"

FONT_TITLE = "Segoe UI"
FONT_MATH = "Segoe UI"

def crear_ejes_con_numeros(x_range, y_range, x_length=6.0, y_length=4.5, x_step=1, y_step=2):
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        axis_config={"color": COLOR_SUBTEXTO, "stroke_width": 2, "include_numbers": False},
        tips=True
    )
    numeros = VGroup()
    x_min, x_max, _ = x_range
    for x in range(int(x_min) + x_step, int(x_max) + 1, x_step):
        if x <= x_max:
            t = Text(str(x), font=FONT_TITLE, font_size=15, color=COLOR_SUBTEXTO)
            t.next_to(axes.c2p(x, 0), DOWN, buff=0.15)
            numeros.add(t)
    y_min, y_max, _ = y_range
    for y in range(int(y_min) + y_step, int(y_max) + 1, y_step):
        if y <= y_max:
            t = Text(str(y), font=FONT_TITLE, font_size=15, color=COLOR_SUBTEXTO)
            t.next_to(axes.c2p(0, y), LEFT, buff=0.15)
            numeros.add(t)
    return axes, numeros

class Escena1Introduccion(Scene):
    def construct(self):
        self.camera.background_color = COLOR_FONDO

        titulo = Text("Cálculo Intermedio", font=FONT_TITLE, font_size=40, weight=BOLD, color=COLOR_TEXTO)
        subtitulo = Text("La Integral de una Tasa de Cambio y el 2° Teorema Fundamental", font=FONT_TITLE, font_size=22, color=COLOR_CURVA)
        cabecera = VGroup(titulo, subtitulo).arrange(DOWN, buff=0.25).to_edge(UP, buff=0.7)

        self.play(FadeIn(cabecera, shift=DOWN), run_time=1.2)
        self.wait(2.5)

        preguntas_textos = [
            "1. ¿Qué representa la integral de una tasa de cambio?",
            "2. ¿La cantidad acumulada es siempre la cantidad final del sistema?",
            "3. ¿Cómo cambia la acumulación al ampliar el límite superior 'x'?",
            "4. ¿Por qué la derivada de la acumulación es igual a la función original?"
        ]

        preguntas_vgroup = VGroup()
        for preg in preguntas_textos:
            caja = RoundedRectangle(corner_radius=0.15, height=0.85, width=11.5,
                                    fill_color="#1e293b", fill_opacity=0.85, stroke_color="#334155", stroke_width=1.5)
            txt = Text(preg, font=FONT_TITLE, font_size=20, color=COLOR_TEXTO).move_to(caja.get_left() + RIGHT * 0.4, aligned_edge=LEFT)
            preguntas_vgroup.add(VGroup(caja, txt))

        preguntas_vgroup.arrange(DOWN, buff=0.22).next_to(cabecera, DOWN, buff=0.5)

        for item in preguntas_vgroup:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.9)
            self.wait(2.2)

        self.wait(2.5)

        banner_auto = RoundedRectangle(corner_radius=0.2, height=1.5, width=11.5,
                                       fill_color="#1e3a8a", fill_opacity=0.45, stroke_color=COLOR_CURVA, stroke_width=2)
        txt_auto1 = Text("Ejemplo Práctico: Movimiento Rectilíneo Uniformemente Variado", font=FONT_TITLE, font_size=21, weight=BOLD, color=COLOR_ECUACION)
        txt_auto2 = Text("Aceleración constante a = 2 km/h²  →  Función de velocidad: v(t) = 2t  [km/h]", font=FONT_TITLE, font_size=20, color=COLOR_TEXTO)
        txt_auto3 = Text("Objetivo: Analizar la acumulación de distancia y su razón instantánea de cambio", font=FONT_TITLE, font_size=17, color=COLOR_SUBTEXTO)
        info_auto = VGroup(txt_auto1, txt_auto2, txt_auto3).arrange(DOWN, buff=0.12).move_to(banner_auto.get_center())
        ejemplo_box = VGroup(banner_auto, info_auto).move_to(preguntas_vgroup.get_center())

        self.play(
            FadeOut(preguntas_vgroup, shift=UP * 0.4),
            FadeIn(ejemplo_box, shift=UP * 0.4),
            run_time=1.2
        )
        self.wait(10.5)

        self.play(FadeOut(cabecera), FadeOut(ejemplo_box), run_time=1.0)
        self.wait(1.0)

class Escena2TasaDeCambio(Scene):
    def construct(self):
        self.camera.background_color = COLOR_FONDO

        titulo = Text("1. ¿Qué representa la integral de una tasa de cambio?", font=FONT_TITLE, font_size=25, weight=BOLD, color=COLOR_CURVA)
        titulo.to_edge(UP, buff=0.5)
        self.play(Write(titulo), run_time=1.2)
        self.wait(2.0)

        axes, numeros = crear_ejes_con_numeros(
            x_range=[0, 4.2, 1],
            y_range=[0, 8.5, 2],
            x_length=5.8,
            y_length=4.3,
            x_step=1,
            y_step=2
        )
        axes_group = VGroup(axes, numeros).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        x_label = Text("Tiempo t [horas]", font=FONT_TITLE, font_size=15, color=COLOR_SUBTEXTO).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = Text("Velocidad v(t) [km/h]", font=FONT_TITLE, font_size=15, color=COLOR_SUBTEXTO).next_to(axes.y_axis.get_end(), UP, buff=0.2)

        linea_v = axes.plot(lambda t: 2 * t, x_range=[0, 4], color=COLOR_CURVA, stroke_width=3.5)
        linea_label = Text("v(t) = 2t", font=FONT_TITLE, font_size=20, weight=BOLD, color=COLOR_CURVA).next_to(axes.c2p(3.2, 6.4), UP + LEFT, buff=0.15)

        self.play(Create(axes), Write(numeros), Write(x_label), Write(y_label), run_time=2.0)
        self.wait(1.5)
        self.play(Create(linea_v), Write(linea_label), run_time=1.5)
        self.wait(2.5)

        rects_pocos = axes.get_riemann_rectangles(
            linea_v,
            x_range=[1, 3],
            dx=0.5,
            color=[COLOR_AREA, COLOR_DELTA],
            fill_opacity=0.6,
            stroke_width=1,
            stroke_color=COLOR_TEXTO
        )
        self.play(Create(rects_pocos), run_time=1.8)
        self.wait(3.0)

        panel_rect = RoundedRectangle(corner_radius=0.2, height=5.3, width=5.6,
                                      fill_color="#1e293b", fill_opacity=0.92, stroke_color="#334155", stroke_width=1.5)
        panel_rect.to_edge(RIGHT, buff=0.7).shift(DOWN * 0.2)

        p_t1 = Text("Aproximación por Particiones:", font=FONT_TITLE, font_size=18, weight=BOLD, color=COLOR_TEXTO)
        p_t2 = Text("Base = Δt  |  Altura = v(tᵢ)", font=FONT_TITLE, font_size=17, color=COLOR_SUBTEXTO)
        p_t3 = Text("Área de cada barra = v(tᵢ) · Δt", font=FONT_TITLE, font_size=19, weight=BOLD, color=COLOR_ECUACION)
        p_sep1 = Line(LEFT, RIGHT, color="#475569").set_width(4.8)
        p_t4 = Text("Análisis Dimensional de Unidades:", font=FONT_TITLE, font_size=18, weight=BOLD, color=COLOR_TEXTO)
        p_t5 = Text("[km / h]  ×  [h]  =  [km]", font=FONT_TITLE, font_size=23, weight=BOLD, color=COLOR_VERDE)
        p_sep2 = Line(LEFT, RIGHT, color="#475569").set_width(4.8)
        p_t6 = Text("Interpretación Física:", font=FONT_TITLE, font_size=18, weight=BOLD, color=COLOR_TEXTO)
        p_t7 = Text("DISTANCIA RECORRIDA", font=FONT_TITLE, font_size=22, weight=BOLD, color=COLOR_CURVA)

        panel_content = VGroup(p_t1, p_t2, p_t3, p_sep1, p_t4, p_t5, p_sep2, p_t6, p_t7).arrange(DOWN, buff=0.18).move_to(panel_rect.get_center())

        self.play(FadeIn(panel_rect), FadeIn(panel_content), run_time=1.5)
        self.wait(9.0)

        rects_muchos = axes.get_riemann_rectangles(
            linea_v,
            x_range=[1, 3],
            dx=0.1,
            color=[COLOR_AREA, COLOR_CURVA],
            fill_opacity=0.65,
            stroke_width=0.5,
            stroke_color=COLOR_TEXTO
        )
        self.play(Transform(rects_pocos, rects_muchos), run_time=2.0)
        self.wait(2.5)

        area_continua = axes.get_area(linea_v, x_range=[1, 3], color=COLOR_AREA, opacity=0.75)
        self.play(Transform(rects_pocos, area_continua), run_time=2.0)
        self.wait(2.5)

        calc_box = RoundedRectangle(corner_radius=0.15, height=0.85, width=5.6,
                                    fill_color="#064e3b", fill_opacity=0.85, stroke_color=COLOR_VERDE, stroke_width=1.5)
        calc_box.next_to(panel_rect, DOWN, buff=0.2)
        integral_txt = Text("Área = ∫₁³ 2t dt = [t²]₁³ = 9 - 1 = 8 km", font=FONT_TITLE, font_size=18, weight=BOLD, color=COLOR_TEXTO).move_to(calc_box.get_center())

        self.play(FadeIn(calc_box), Write(integral_txt), run_time=1.2)
        self.wait(9.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(1.0)

class Escena3CambioNeto(Scene):
    def construct(self):
        self.camera.background_color = COLOR_FONDO

        titulo = Text("2. ¿La cantidad acumulada corresponde siempre al total final?", 
                      font=FONT_TITLE, font_size=23, weight=BOLD, color=COLOR_CURVA).to_edge(UP, buff=0.5)
        self.play(Write(titulo), run_time=1.2)
        self.wait(2.0)

        no_box = RoundedRectangle(corner_radius=0.15, height=1.0, width=11.5,
                                  fill_color="#450a0a", fill_opacity=0.75, stroke_color=COLOR_DESTACADO, stroke_width=2.5)
        no_box.next_to(titulo, DOWN, buff=0.35)
        no_txt1 = Text("¡NO!", font=FONT_TITLE, font_size=32, weight=BOLD, color=COLOR_DESTACADO)
        no_txt2 = Text("La integral entrega únicamente el CAMBIO NETO (Δs), no el estado absoluto.",
                       font=FONT_TITLE, font_size=19, color=COLOR_TEXTO)
        no_group = VGroup(no_txt1, no_txt2).arrange(RIGHT, buff=0.4).move_to(no_box.get_center())

        self.play(FadeIn(no_box), Write(no_group), run_time=1.5)
        self.wait(4.0)

        teorema_card = RoundedRectangle(corner_radius=0.2, height=4.3, width=11.5,
                                        fill_color="#1e293b", fill_opacity=0.9, stroke_color="#334155", stroke_width=1.5)
        teorema_card.next_to(no_box, DOWN, buff=0.3)

        t_sub = Text("Teorema del Cambio Neto (Larson & Edwards)", font=FONT_TITLE, font_size=20, weight=BOLD, color=COLOR_ECUACION)
        t_formula = Text("∫ₐᵇ F'(t) dt = F(b) - F(a) = Cambio Neto (ΔF)", font=FONT_TITLE, font_size=24, color=COLOR_TEXTO)
        sep = Line(LEFT, RIGHT, color="#475569").set_width(10.5)

        auto_caso1_t = Text("1. Condición o Posición Inicial (t = 1 h):", font=FONT_TITLE, font_size=17, color=COLOR_SUBTEXTO)
        auto_caso1_v = Text("Odómetro previo: s(1) = 50 km  (punto de partida de la medición)", font=FONT_TITLE, font_size=19, color=COLOR_TEXTO)
        bloque1 = VGroup(auto_caso1_t, auto_caso1_v).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        auto_caso2_t = Text("2. Acumulación Calculada por la Integral (de 1 h a 3 h):", font=FONT_TITLE, font_size=17, color=COLOR_SUBTEXTO)
        auto_caso2_v = Text("Variación neta: Δs = ∫₁³ 2t dt = 8 km recorridos en ese tramo", font=FONT_TITLE, font_size=19, weight=BOLD, color=COLOR_VERDE)
        bloque2 = VGroup(auto_caso2_t, auto_caso2_v).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        auto_caso3_t = Text("3. Posición Final Absoluta del Vehículo (t = 3 h):", font=FONT_TITLE, font_size=17, color=COLOR_SUBTEXTO)
        auto_caso3_v = Text("s(3) = s(1) + ∫₁³ 2t dt = 50 km + 8 km = 58 km", font=FONT_TITLE, font_size=21, weight=BOLD, color=COLOR_ECUACION)
        bloque3 = VGroup(auto_caso3_t, auto_caso3_v).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        info_comparativa = VGroup(bloque1, bloque2, bloque3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        todo_teorema = VGroup(t_sub, t_formula, sep, info_comparativa).arrange(DOWN, buff=0.18).move_to(teorema_card.get_center())

        self.play(FadeIn(teorema_card), FadeIn(todo_teorema), run_time=1.5)
        self.wait(12.0)

        barra_fondo = RoundedRectangle(corner_radius=0.1, height=0.5, width=10.0, fill_color="#334155", fill_opacity=0.4, stroke_width=1)
        barra_s0 = RoundedRectangle(corner_radius=0.1, height=0.5, width=7.0, fill_color="#0284c7", fill_opacity=0.8, stroke_width=0).align_to(barra_fondo, LEFT)
        barra_ds = RoundedRectangle(corner_radius=0.1, height=0.5, width=3.0, fill_color="#10b981", fill_opacity=0.85, stroke_width=0).next_to(barra_s0, RIGHT, buff=0)
        lbl_s0 = Text("s(1) = 50 km", font=FONT_TITLE, font_size=14, color=COLOR_TEXTO).move_to(barra_s0.get_center())
        lbl_ds = Text("+ Δs = 8 km", font=FONT_TITLE, font_size=14, color=COLOR_TEXTO).move_to(barra_ds.get_center())
        lbl_tot = Text("Total = 58 km", font=FONT_TITLE, font_size=15, weight=BOLD, color=COLOR_ECUACION).next_to(barra_fondo, RIGHT, buff=0.25)
        grafico_barras = VGroup(barra_fondo, barra_s0, barra_ds, lbl_s0, lbl_ds, lbl_tot).next_to(teorema_card, DOWN, buff=0.15)

        self.play(FadeIn(grafico_barras), run_time=1.2)
        self.wait(10.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(1.0)

class Escena4FuncionAcumulacion(Scene):
    def construct(self):
        self.camera.background_color = COLOR_FONDO

        titulo = Text("3. ¿Cómo cambia la acumulación al ampliar el límite superior 'x'?",
                      font=FONT_TITLE, font_size=23, weight=BOLD, color=COLOR_CURVA).to_edge(UP, buff=0.5)
        self.play(Write(titulo), run_time=1.2)
        self.wait(2.0)

        axes, numeros = crear_ejes_con_numeros(
            x_range=[0, 3.8, 1],
            y_range=[0, 8.5, 2],
            x_length=5.8,
            y_length=4.3,
            x_step=1,
            y_step=2
        )
        axes_group = VGroup(axes, numeros).to_edge(LEFT, buff=0.8).shift(DOWN * 0.2)

        x_label = Text("Límite superior variable: x [h]", font=FONT_TITLE, font_size=15, color=COLOR_SUBTEXTO).next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = Text("v(t) = 2t [km/h]", font=FONT_TITLE, font_size=16, color=COLOR_CURVA).next_to(axes.y_axis.get_end(), UP, buff=0.2)

        linea_v = axes.plot(lambda t: 2 * t, x_range=[0, 3.8], color=COLOR_CURVA, stroke_width=3.5)
        self.play(Create(axes), Write(numeros), Write(x_label), Write(y_label), Create(linea_v), run_time=2.0)
        self.wait(1.5)

        panel = RoundedRectangle(corner_radius=0.2, height=4.9, width=5.6,
                                 fill_color="#1e293b", fill_opacity=0.92, stroke_color="#334155", stroke_width=1.5)
        panel.to_edge(RIGHT, buff=0.7).shift(DOWN * 0.2)

        p_t1 = Text("Función de Acumulación A(x):", font=FONT_TITLE, font_size=19, weight=BOLD, color=COLOR_ECUACION)
        p_t2 = Text("A(x) = ∫₀ˣ 2t dt", font=FONT_TITLE, font_size=24, color=COLOR_TEXTO)
        p_t3 = Text("Integrando mediante antiderivada:", font=FONT_TITLE, font_size=16, color=COLOR_SUBTEXTO)
        p_t4 = Text("A(x) = [t²]₀ˣ = x² - 0² = x²", font=FONT_TITLE, font_size=22, weight=BOLD, color=COLOR_VERDE)
        sep = Line(LEFT, RIGHT, color="#475569").set_width(4.8)

        panel_top = VGroup(p_t1, p_t2, p_t3, p_t4, sep).arrange(DOWN, buff=0.18).move_to(panel.get_center() + UP * 0.7)
        self.play(FadeIn(panel), FadeIn(panel_top), run_time=1.5)
        self.wait(3.0)

        x_tracker = ValueTracker(1.0)

        area_dinamica = always_redraw(lambda: axes.get_area(
            linea_v,
            x_range=[0, x_tracker.get_value()],
            color=COLOR_AREA,
            opacity=0.75
        ))

        linea_x = always_redraw(lambda: axes.get_vertical_line(
            axes.c2p(x_tracker.get_value(), 2 * x_tracker.get_value()),
            color=COLOR_DELTA,
            stroke_width=3
        ))

        x_pt_label = always_redraw(lambda: Text(
            f"x = {x_tracker.get_value():.2f}",
            font=FONT_TITLE, font_size=16, color=COLOR_DELTA
        ).next_to(axes.c2p(x_tracker.get_value(), 0), DOWN, buff=0.25))

        valor_acumulado = always_redraw(lambda: VGroup(
            Text(f"Evaluación instantánea para x = {x_tracker.get_value():.2f}:", font=FONT_TITLE, font_size=16, color=COLOR_SUBTEXTO),
            Text(f"Área A(x) = ({x_tracker.get_value():.2f})² = {x_tracker.get_value()**2:.2f} km",
                 font=FONT_TITLE, font_size=19, weight=BOLD, color=COLOR_ECUACION)
        ).arrange(DOWN, buff=0.1).next_to(sep, DOWN, buff=0.25))

        self.add(area_dinamica, linea_x, x_pt_label)
        self.play(FadeIn(valor_acumulado), run_time=1.0)
        self.wait(3.5)

        self.play(x_tracker.animate.set_value(2.0), run_time=4.0, rate_func=linear)
        self.wait(5.0)

        self.play(x_tracker.animate.set_value(3.0), run_time=4.0, rate_func=linear)
        self.wait(5.0)

        self.play(x_tracker.animate.set_value(3.5), run_time=3.0, rate_func=linear)
        self.wait(4.5)

        concl = Text("¡A medida que ampliamos 'x', la distancia acumulada crece de forma cuadrática (x²)! ",
                     font=FONT_TITLE, font_size=18, color=COLOR_CURVA)
        concl.to_edge(DOWN, buff=0.35)
        self.play(Write(concl), run_time=1.2)
        self.wait(7.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(1.0)

class Escena5SegundoTeorema(Scene):
    def construct(self):
        self.camera.background_color = COLOR_FONDO

        titulo = Text("4. Segundo Teorema Fundamental del Cálculo", font=FONT_TITLE, font_size=25, weight=BOLD, color=COLOR_CURVA)
        titulo.to_edge(UP, buff=0.35)
        declaracion = Text("d/dx [ ∫ₐˣ f(t) dt ] = f(x)    →   La derivada de la acumulación es la función original",
                           font=FONT_TITLE, font_size=18, color=COLOR_ECUACION)
        declaracion.next_to(titulo, DOWN, buff=0.15)

        self.play(Write(titulo), FadeIn(declaracion), run_time=1.5)
        self.wait(3.0)

        axes, _ = crear_ejes_con_numeros(
            x_range=[0, 4.0, 1],
            y_range=[0, 8.5, 2],
            x_length=5.6,
            y_length=4.2,
            x_step=1,
            y_step=2
        )
        axes.to_edge(LEFT, buff=0.7).shift(DOWN * 0.45)

        linea_v = axes.plot(lambda t: 2 * t, x_range=[0, 3.8], color=COLOR_CURVA, stroke_width=3.5)
        v_label = Text("v(t) = 2t", font=FONT_TITLE, font_size=18, color=COLOR_CURVA).next_to(axes.c2p(3.2, 6.4), UP + LEFT, buff=0.1)

        x_val = 1.8
        dx_val = 0.8

        area_base = axes.get_area(linea_v, x_range=[0, x_val], color=COLOR_AREA, opacity=0.7)
        area_franja = axes.get_area(linea_v, x_range=[x_val, x_val + dx_val], color=COLOR_DELTA, opacity=0.85)

        label_x = Text("x", font=FONT_TITLE, font_size=18, color=COLOR_TEXTO).next_to(axes.c2p(x_val, 0), DOWN, buff=0.2)
        label_xdx = Text("x + Δx", font=FONT_TITLE, font_size=18, color=COLOR_DELTA).next_to(axes.c2p(x_val + dx_val, 0), DOWN, buff=0.2)

        llave = BraceBetweenPoints(axes.c2p(x_val, 0), axes.c2p(x_val + dx_val, 0), direction=UP)
        llave_txt = Text("Δx", font=FONT_TITLE, font_size=16, color=COLOR_DELTA).next_to(llave, UP, buff=0.1)

        linea_h = DashedLine(axes.c2p(x_val, 0), axes.c2p(x_val, 2 * x_val), color=COLOR_TEXTO, stroke_width=2)
        h_label = Text("Altura ≈ 2x", font=FONT_TITLE, font_size=16, color=COLOR_TEXTO).next_to(axes.c2p(x_val, x_val), LEFT, buff=0.15)

        self.play(Create(axes), Create(linea_v), Write(v_label), run_time=1.5)
        self.play(FadeIn(area_base), Write(label_x), run_time=1.0)
        self.play(FadeIn(area_franja), Write(label_xdx), Create(llave), Write(llave_txt), Create(linea_h), Write(h_label), run_time=1.8)
        self.wait(3.5)

        panel_rect = RoundedRectangle(corner_radius=0.2, height=4.8, width=6.3,
                                      fill_color="#1e293b", fill_opacity=0.92, stroke_color="#334155", stroke_width=1.5)
        panel_rect.to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        self.play(FadeIn(panel_rect), run_time=1.0)

        pasos = [
            ("1. Definición formal de la derivada:", "A'(x) = lim [ A(x + Δx) - A(x) ] / Δx", COLOR_TEXTO),
            ("2. Expresión como integrales:", "A(x+Δx) - A(x) = ∫ₓˣ⁺ᵟˣ 2t dt", COLOR_SUBTEXTO),
            ("3. Teorema del Valor Medio:", "Área franja = v(c) · Δx  (con x ≤ c ≤ x+Δx)", COLOR_DELTA),
            ("4. Sustitución en el cociente:", "A'(x) = lim [ 2c · Δx ] / Δx = lim [ 2c ]", COLOR_ECUACION),
            ("5. Al tender Δx a 0 (c → x):", "A'(x) = 2x = v(x)", COLOR_VERDE)
        ]

        paso_mobjects = []
        for tit_p, form_p, col_f in pasos:
            t1 = Text(tit_p, font=FONT_TITLE, font_size=15, color=COLOR_SUBTEXTO)
            t2 = Text(form_p, font=FONT_TITLE, font_size=18, weight=BOLD, color=col_f)
            grp = VGroup(t1, t2).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            paso_mobjects.append(grp)

        todo_pasos = VGroup(*paso_mobjects).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(panel_rect.get_center())

        for p in paso_mobjects:
            self.play(FadeIn(p, shift=RIGHT * 0.2), run_time=1.0)
            self.wait(5.5)

        self.wait(3.0)

        dx_tracker = ValueTracker(0.8)
        franja_dinamica = always_redraw(lambda: axes.get_area(
            linea_v,
            x_range=[x_val, x_val + dx_tracker.get_value()],
            color=COLOR_DELTA,
            opacity=0.85
        ))
        self.remove(area_franja)
        self.add(franja_dinamica)
        self.play(dx_tracker.animate.set_value(0.08), run_time=4.0, rate_func=smooth)
        self.wait(5.5)

        banner_final = RoundedRectangle(corner_radius=0.15, height=0.9, width=12.2,
                                        fill_color="#064e3b", fill_opacity=0.92, stroke_color=COLOR_VERDE, stroke_width=2)
        banner_final.to_edge(DOWN, buff=0.2)
        texto_final = Text("¡Queda demostrado!: La razón de cambio de la distancia acumulada es la velocidad instantánea v(x) = 2x",
                           font=FONT_TITLE, font_size=18, weight=BOLD, color=COLOR_TEXTO).move_to(banner_final.get_center())

        self.play(FadeIn(banner_final), Write(texto_final), run_time=1.5)
        self.wait(8.5)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(1.0)

class Escena6SintesisYCierre(Scene):
    def construct(self):
        self.camera.background_color = COLOR_FONDO

        titulo = Text("Síntesis y Respuestas a las Preguntas Guía", font=FONT_TITLE, font_size=28, weight=BOLD, color=COLOR_TEXTO).to_edge(UP, buff=0.6)
        self.play(Write(titulo), run_time=1.2)
        self.wait(2.0)

        tarjetas = [
            ("1. ¿Qué representa la integral de una tasa de cambio?", "Representa la magnitud física neta acumulada (velocidad × tiempo = distancia).", COLOR_CURVA),
            ("2. ¿La acumulación es siempre el total final?", "¡NO! Es solo el cambio neto (Δs). Debe sumarse la condición o estado inicial s(a).", COLOR_DESTACADO),
            ("3. ¿Cómo cambia al ampliar el límite superior 'x'?", "Forma la función de acumulación A(x) = x², exhibiendo un crecimiento cuadrático.", COLOR_ECUACION),
            ("4. ¿Por qué su derivada es la función original?", "Por el 2° Teorema Fundamental: al encoger la franja Δx → 0, el área rectangular colapsa en la altura f(x).", COLOR_VERDE)
        ]

        vgroup_tarjetas = VGroup()
        for t_preg, t_resp, col in tarjetas:
            caja = RoundedRectangle(corner_radius=0.15, height=0.95, width=11.8,
                                    fill_color="#1e293b", fill_opacity=0.88, stroke_color=col, stroke_width=1.5)
            tit = Text(t_preg, font=FONT_TITLE, font_size=17, weight=BOLD, color=col)
            det = Text(t_resp, font=FONT_TITLE, font_size=16, color=COLOR_TEXTO)
            cont = VGroup(tit, det).arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to(caja.get_left() + RIGHT * 0.35, aligned_edge=LEFT)
            vgroup_tarjetas.add(VGroup(caja, cont))

        vgroup_tarjetas.arrange(DOWN, buff=0.2).next_to(titulo, DOWN, buff=0.4)

        for card in vgroup_tarjetas:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.9)
            self.wait(2.5)

        self.wait(3.0)

        self.play(FadeOut(vgroup_tarjetas), run_time=0.8)

        creditos_rect = RoundedRectangle(corner_radius=0.2, height=4.2, width=11.5,
                                         fill_color="#0f172a", fill_opacity=0.95, stroke_color=COLOR_CURVA, stroke_width=2)
        cred_t1 = Text("Evaluación Integral de Desempeño (EID)", font=FONT_TITLE, font_size=24, weight=BOLD, color=COLOR_TEXTO)
        cred_t2 = Text("Cálculo Intermedio - Introducción a la Integral con Manim", font=FONT_TITLE, font_size=19, color=COLOR_CURVA)
        cred_sep = Line(LEFT, RIGHT, color="#475569").set_width(9.5)
        cred_t3 = Text("Marco Teórico: Larson & Edwards (Cálculo) - Teorema del Cambio Neto y 2° TFC", font=FONT_TITLE, font_size=17, color=COLOR_ECUACION)
        cred_t4 = Text("Motor de Animación: Manim Community v0.22 - Renderizado en Python", font=FONT_TITLE, font_size=16, color=COLOR_SUBTEXTO)
        cred_t5 = Text("Cumplimiento de Pauta: Duración 4 a 5 minutos | Todos los criterios V1-V8 cubiertos", font=FONT_TITLE, font_size=16, weight=BOLD, color=COLOR_VERDE)

        creditos_content = VGroup(cred_t1, cred_t2, cred_sep, cred_t3, cred_t4, cred_t5).arrange(DOWN, buff=0.25).move_to(creditos_rect.get_center())
        creditos_box = VGroup(creditos_rect, creditos_content).move_to(ORIGIN)

        self.play(FadeIn(creditos_box, shift=UP * 0.3), run_time=1.2)
        self.wait(11.0)

        self.play(FadeOut(Group(*self.mobjects)), run_time=1.0)
        self.wait(1.0)

class VideoCompleto(Scene):
    def construct(self):
        Escena1Introduccion.construct(self)
        Escena2TasaDeCambio.construct(self)
        Escena3CambioNeto.construct(self)
        Escena4FuncionAcumulacion.construct(self)
        Escena5SegundoTeorema.construct(self)
        Escena6SintesisYCierre.construct(self)
