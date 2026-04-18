from manim import *

class NLPPipelineScene_v3(Scene):
    def construct(self):
        # Configuration
        header_color = BLUE
        
        # 1. TOKENIZATION
        step1_title = Text("1. Tokenization (Subword Splitting)", color=header_color).to_edge(UP)
        word = Text('"unbelievable team"', font="Arial").shift(UP*1.5)
        tokens = Text('["un", "##believ", "##able", "team"]', font="Arial", color=YELLOW).next_to(word, DOWN)
        
        self.play(Write(step1_title), Write(word))
        self.play(TransformFromCopy(word, tokens))
        self.wait(1)

        # 2. TOKEN IDs
        step2_title = Text("2. Token ID Creation (1 x Tn)", color=header_color).to_edge(UP)
        id_list = ["1012", "3056", "2003", "1024"]
        ids_group = VGroup(*[Text(i, font="Arial", color=GREEN).scale(0.8) for i in id_list])
        ids_group.arrange(RIGHT, buff=0.5).next_to(tokens, DOWN)
        
        self.play(Transform(step1_title, step2_title))
        self.play(Write(ids_group))
        self.wait(1)

        # 3. EMBEDDING LOOKUP
        step3_title = Text("3. Embedding Lookup (Tn x d)", color=header_color).to_edge(UP)
        
        matrix_data = [
            ["0.12", "0.85", "-0.3", "0.5"],
            ["0.45", "-0.1", "0.92", "0.1"],
            ["-0.2", "0.33", "0.11", "0.7"],
            ["0.05", "0.60", "-0.15", "0.3"]
        ]
        
        emb_matrix = MobjectMatrix(
            [[Text(x, font="Arial").scale(0.5) for x in row] for row in matrix_data],
            left_bracket="[", right_bracket="]"
        ).shift(RIGHT * 0.8 + DOWN * 0.1)
        
        ids_vertical = VGroup(*[Text(i, font="Arial", color=GREEN).scale(0.6) for i in id_list])
        for i, item in enumerate(ids_vertical):
            item.move_to(emb_matrix.get_rows()[i].get_left() + LEFT * 1.2)

        labels = Text("Rows = Token IDs | Cols = Dimensions (d)", font="Arial").scale(0.4).next_to(emb_matrix, DOWN)

        self.play(
            Transform(step1_title, step3_title),
            FadeOut(word), FadeOut(tokens),
            ReplacementTransform(ids_group, ids_vertical),
            Create(emb_matrix),
            Write(labels)
        )
        self.wait(1)

        # 4. CONTEXTUAL TRANSFORMATION
        step4_title = Text("4. Contextual Transformation (Attention)", color=header_color).to_edge(UP)
        new_values = [
            ["0.15", "0.80", "-0.2", "0.4"],
            ["0.40", "0.10", "0.90", "0.2"],
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


        column_highlights = VGroup()
        for i in range(4): # Since we have 4 dimensions (d)
            # We get the specific column from the updated matrix
            col = emb_matrix.get_columns()[i]
            rect = SurroundingRectangle(col, color=WHITE, buff=0.1)
            column_highlights.add(rect)

        # Show the highlights one by one or all at once
        self.play(Create(column_highlights), run_time=1.5)
        self.wait(1)

        # 5. MEAN POOLING (Aggregation)
        step5_title = Text("5. Mean Pooling Aggregation (1 x d)", color=header_color).to_edge(UP)
        
        # (Your existing mean_data and pooled_vec definitions)
        mean_data = [["0.14", "0.44", "0.19", "0.45"]]
        pooled_vec = MobjectMatrix(
            [[Text(x, font="Arial", color=RED).scale(0.6) for x in row] for row in mean_data],
            left_bracket="[", right_bracket="]"
        ).move_to(emb_matrix)

        final_label = Text("Final Sentence Embedding Vector", font="Arial", color=RED).scale(0.5).next_to(pooled_vec, DOWN)

        self.play(Transform(step1_title, step5_title))
        
        # Modified play call to fade out highlights during the squeeze
        self.play(
            FadeOut(ids_vertical),
            FadeOut(labels),
            FadeOut(column_highlights), # Clean up the rectangles
            Transform(emb_matrix, pooled_vec)
        )
        self.play(Write(final_label))
        self.wait(2)
        
class SimilaritySearch_v1(Scene):
    def construct(self):
        header_color = BLUE
        
        # --- PHASE 1: INITIAL TYPES ---
        topic1 = "1. Cosine Similarity Search"
        topic2 = "2. Euclidean Distance"
        topic3 = "3. Dot Product"

        title_main = Text('Similarity Search Techniques (RAG)', color=header_color).to_edge(UP * 2.5)
        self.play(Write(title_main))

        type1 = Text(f'{topic1}', color=YELLOW).next_to(title_main, DOWN)
        type2 = Text(f'{topic2}', color=YELLOW).next_to(type1, DOWN)
        type3 = Text(f'{topic3}', color=YELLOW).next_to(type2, DOWN)

        self.play(TransformFromCopy(title_main, type1), TransformFromCopy(title_main, type2), TransformFromCopy(title_main, type3) if 'title1' in locals() else TransformFromCopy(title_main, type3))
        self.wait(1) 
        self.play(FadeOut(type1), FadeOut(type2), FadeOut(type3))

        # --- PHASE 2: QUERY & VECTOR DATABASE ---
        db_title = Text("Step 1: Input Processing & Database Lookup", color=header_color).to_edge(UP)
        self.play(Transform(title_main, db_title))

        # 1. Position the Query in the middle, just below the heading
        query_text = Text('Query: "What is the capital of France?"', font="Arial", color=WHITE).scale(0.5)
        query_text.next_to(db_title, DOWN, buff=0.8) # Positioned below heading
        
        query_label = Text("Query Embedding:", font="Arial", color=GRAY).scale(0.3)
        query_vec = Text("[0.11, ..., 0.85]", font="Consolas", color=YELLOW).scale(0.5)
        
        # Group and center the query components horizontally
        query_group = VGroup(query_text, query_label, query_vec).arrange(RIGHT, buff=0.4)
        query_group.move_to(UP * 1.5) # Ensuring it stays in the top-middle area

        self.play(Write(query_text))
        self.play(FadeIn(VGroup(query_label, query_vec), shift=UP))
        self.wait(1)

        # 2. Build the Vector Database below the Query
        sentences = ["Paris...", "Berlin...", "Madrid..."]
        vectors = ["[0.12, ..., 0.88]", "[-0.01, ..., 0.12]", "[0.33, ..., 0.56]"]

        db_rows = VGroup()
        for i in range(3):
            label = Text("Embedding:", font="Arial", color=GRAY).scale(0.3)
            vec_txt = Text(vectors[i], font="Consolas", color=GREEN).scale(0.5)
            sent_txt = Text(f"({sentences[i]})", font="Arial", color=WHITE).scale(0.4)
            row = VGroup(label, vec_txt, sent_txt).arrange(RIGHT, buff=0.3)
            db_rows.add(row)
        
        # Arrange rows vertically and position them below the query group
        db_rows.arrange(DOWN, buff=0.5).next_to(query_group, DOWN, buff=1.0)
        
        self.play(Write(db_rows))
        self.wait(1)

        # --- PHASE 3: TECHNIQUE 1 - COSINE ---
        title_cos = Text(topic1, color=header_color).to_edge(UP)
        self.play(Transform(title_main, title_cos), db_rows[1:].animate.set_opacity(0.2))
        
        # Formula: A·B / ||A||||B||
        num = Text("A · B", color=YELLOW).scale(0.6)
        line = Line(LEFT, RIGHT).scale(0.4)
        den = Text("||A|| ||B||", color=YELLOW).scale(0.6)
        formula_cos = VGroup(num, line, den).arrange(DOWN, buff=0.1).next_to(db_rows[0], RIGHT, buff=0.8)
        score_cos = Text("Score: 0.98", color=GOLD).scale(0.5).next_to(formula_cos, RIGHT)
        
        self.play(Write(formula_cos), Write(score_cos))
        winner_rect = SurroundingRectangle(db_rows[0], color=GOLD)
        self.play(Create(winner_rect))
        self.wait(1)
        self.play(FadeOut(formula_cos), FadeOut(score_cos), FadeOut(winner_rect))

        # --- PHASE 4: TECHNIQUE 2 - EUCLIDEAN DISTANCE ---
        title_euc = Text(topic2, color=header_color).to_edge(UP)
        self.play(Transform(title_main, title_euc))

        # We build the L2 formula: √Σ(Ai - Bi)²
        # Building the base text
        base_math = Text("Σ(Ai - Bi)", font="Arial", color=GOLD).scale(0.5)
        
        # Creating the square root symbol
        sqrt_sym = Text("√", font="Arial", color=GOLD).scale(0.8)
        
        # Creating the '2' for the exponent
        exponent = Text("2", font="Arial", color=GOLD).scale(0.3)
        
        # Position exponent to the top right of the base math
        exponent.next_to(base_math, UR, buff=0.05)
        
        # Group base and exponent to define the root bar length
        math_content = VGroup(base_math, exponent)
        sqrt_sym.next_to(math_content, LEFT, buff=0.1)
        
        # Draw the bar over the top of the math
        root_bar = Line(
            sqrt_sym.get_corner(UP+RIGHT), 
            math_content.get_corner(UP+RIGHT) + RIGHT*0.1, 
            stroke_width=2
        )

        # Final formula group
        formula_euc = VGroup(sqrt_sym, root_bar, math_content).next_to(db_rows[0], RIGHT, buff=0.8)
        score_euc = Text("Dist:0.02", color=GOLD).scale(0.5).next_to(formula_euc, RIGHT, buff=0.4)

        # Execution
        self.play(Write(formula_euc), Write(score_euc))
        
        # Highlight winner (Lower is better for Euclidean distance)
        winner_rect = SurroundingRectangle(db_rows[0], color=GOLD)
        self.play(Create(winner_rect))
        
        self.wait(1)
        self.play(FadeOut(formula_euc), FadeOut(score_euc), FadeOut(winner_rect))

        # --- PHASE 5: TECHNIQUE 3 - DOT PRODUCT ---
        title_dot = Text(topic3, color=header_color).to_edge(UP)
        self.play(Transform(title_main, title_dot))
        
        # Formula: A · B
        formula_dot = Text("A · B", color=YELLOW).scale(0.7).next_to(db_rows[0], RIGHT, buff=0.8)
        score_dot = Text("Score: 12.4", color=GOLD).scale(0.5).next_to(formula_dot, RIGHT)
        
        self.play(Write(formula_dot), Write(score_dot))
        self.play(Create(winner_rect))
        self.wait(2)

        # --- CONTINUING FROM DOT PRODUCT WINNER ---
        # 1. Show scores for the remaining rows to show the 'Search' process
        other_scores = ["Score: 4.2", "Score: 6.1"]
        score_group = VGroup()
        
        self.play(db_rows[1:].animate.set_opacity(1.0)) # Bring other rows back to focus
        
        for i, score_val in enumerate(other_scores, start=1):
            s = Text(score_val, color=GOLD).scale(0.5).next_to(db_rows[i], RIGHT, buff=1.0)
            score_group.add(s)
            self.play(Write(s), run_time=0.5)

        self.wait(1)

        # 2. Top-K Retrieval Animation (Pulling the winner)
        # Clear the 'math' clutter to focus on the result
        self.play(
            FadeOut(score_dot), 
            FadeOut(formula_dot), 
            FadeOut(score_group),
            FadeOut(db_rows[1:]), # Remove non-matching rows
            FadeOut(query_group),
            winner_rect.animate.set_color(GREEN)
        )

        # Move the winning embedding to the center
        winning_row = VGroup(db_rows[0], winner_rect)
        self.play(winning_row.animate.center().shift(UP * 0.2))

        # 3. Final RAG Output
        rag_title = Text("Step 2: Generate Final Answer", color=header_color).to_edge(UP)
        self.play(Transform(title_main, rag_title))

        final_answer = Text(
            'Answer: "The capital of France is Paris."', 
            font="Arial", 
            color=GREEN
        ).scale(0.7).next_to(winning_row, DOWN, buff=1.0)
        self.play(Write(final_answer))
        
        self.wait(3)