from manim import *

class NLPPipelineScene_v1(Scene):
    def construct(self):
        # Configuration
        header_color = BLUE
        
        # 1. TOKENIZATION
        step1_title = Text("1. Tokenization", color=header_color).to_edge(UP)
        word = Text('"unbelievable team"', font="Arial").shift(UP*1.5)
        tokens = Text('["un", "##believ", "##able", "team"]', font="Arial", color=YELLOW).next_to(word, DOWN)
        
        self.play(Write(step1_title), Write(word))
        self.play(TransformFromCopy(word, tokens))
        self.wait(1)

        # 2. TOKEN IDs
        step2_title = Text("2. Token ID Creation", color=header_color).to_edge(UP)
        # We create these as individual objects for easier vertical alignment later
        id_list = ["1012", "3056", "2003", "1024"]
        ids_group = VGroup(*[Text(i, font="Arial", color=GREEN).scale(0.8) for i in id_list])
        ids_group.arrange(RIGHT, buff=0.5).next_to(tokens, DOWN)
        
        self.play(Transform(step1_title, step2_title))
        self.play(Write(ids_group))
        self.wait(1)

        # 3. EMBEDDING GENERATION (Lookup)
        step3_title = Text("3. Embedding Lookup (V x d)", color=header_color).to_edge(UP)
        
        matrix_data = [
            ["0.12", "0.85", "-0.3", "0.5"],
            ["0.45", "-0.1", "0.92", "0.1"],
            ["-0.2", "0.33", "0.11", "0.7"],
            ["0.05", "0.60", "-0.15", "0.3"]
        ]
        
        emb_matrix = MobjectMatrix(
            [[Text(x, font="Arial").scale(0.5) for x in row] for row in matrix_data],
            left_bracket="[", right_bracket="]"
        ).shift(RIGHT * 0.8 + DOWN * 0.1) # Shifted right to make room for IDs
        
        # Repositioning IDs vertically to align with matrix rows
        ids_vertical = VGroup(*[Text(i, font="Arial", color=GREEN).scale(0.6) for i in id_list])
        for i, item in enumerate(ids_vertical):
            item.move_to(emb_matrix.get_rows()[i].get_left() + LEFT * 1.2)

        labels = Text("Rows = Token ID's | Cols = Dimensions (d)", font="Arial").scale(0.4).next_to(emb_matrix, DOWN)

        self.play(
            Transform(step1_title, step3_title),
            FadeOut(word), FadeOut(tokens),
            ReplacementTransform(ids_group, ids_vertical),
            Create(emb_matrix),
            Write(labels)
        )
        self.wait(1)

        # 4. SELF-ATTENTION (Contextual Update)
        step4_title = Text("4. Self-Attention Transformation", color=header_color).to_edge(UP)
        new_values = [
            ["0.15", "0.80", "-0.2", "0.4"],
            ["0.40", "-0.0", "0.90", "0.2"],
            ["-0.1", "0.30", "0.15", "0.8"],
            ["0.10", "0.55", "-0.1", "0.4"]
        ]
        updated_matrix = MobjectMatrix(
            [[Text(x, font="Arial", color=GOLD).scale(0.5) for x in row] for row in new_values],
            left_bracket="[", right_bracket="]"
        ).move_to(emb_matrix)

        self.play(Transform(step1_title, step4_title))
        self.play(Transform(emb_matrix, updated_matrix))
        self.wait(1)

        # 5. MAX POOLING (Aggregation)
        step5_title = Text("5. Max Pooling (1 x d)", color=header_color).to_edge(UP)
        pooled_data = [["0.40", "0.80", "0.90", "0.8"]]
        pooled_vec = MobjectMatrix(
            [[Text(x, font="Arial", color=RED).scale(0.6) for x in row] for row in pooled_data],
            left_bracket="[", right_bracket="]"
        ).move_to(emb_matrix)
        
        final_label = Text("Final Sentence Embedding", font="Arial", color=RED).scale(0.5).next_to(pooled_vec, DOWN)

        self.play(Transform(step1_title, step5_title))
        self.play(
            FadeOut(ids_vertical),
            FadeOut(labels),
            Transform(emb_matrix, pooled_vec)
        )
        self.play(Write(final_label))
        self.wait(2)