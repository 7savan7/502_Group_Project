class Interpreter:
    def __init__(self):
        self.variables = {}

    def eval(self, node):
        if node is None:
            return None

        node_type = node[0]

        if node_type == 'program':
            for stmt in node[1]:
                self.eval(stmt)

        elif node_type == 'declare':
            _, var_type, var_name = node
            self.variables[var_name] = None

        elif node_type == 'assign':
            _, var_name, expr = node
            value = self.eval(expr)
            self.variables[var_name] = value

        elif node_type == 'print':
            value = self.eval(node[1])
            print(value)

        elif node_type == 'ternary':
            _, cond, true_expr, false_expr = node
            return self.eval(true_expr) if self.eval(cond) else self.eval(false_expr)

        elif node_type == 'logical_op':
            _, op, left, right = node
            if op == '&':
                return self.eval(left) and self.eval(right)
            elif op == '|':
                return self.eval(left) or self.eval(right)

        elif node_type == 'relational_op':
            _, op, left, right = node
            l_val = self.eval(left)
            r_val = self.eval(right)
            if op == 'badaHai':
                return l_val > r_val
            elif op == 'chhotaHai':
                return l_val < r_val
            elif op == 'barabarHai':
                return l_val == r_val

        elif node_type == 'binary_op':
            _, op, left, right = node
            l_val = self.eval(left)
            r_val = self.eval(right)
            if op == 'jodo':
                return l_val + r_val
            elif op == 'ghatao':
                return l_val - r_val
            elif op == 'guna':
                return l_val * r_val
            elif op == 'bhaag':
                return l_val // r_val

        elif node_type == 'unary_op':
            _, op, var = node
            if op == '++':
                self.variables[var] += 1
                return self.variables[var]
            elif op == '--':
                self.variables[var] -= 1
                return self.variables[var]

        elif node_type == 'number':
            return node[1]
        elif node_type == 'string':
            return node[1]
        elif node_type == 'bool':
            return node[1] == 'true'
        elif node_type == 'var':
            return self.variables.get(node[1], None)

        elif node_type == 'if_else':
            _, cond, true_block, false_block = node
            if self.eval(cond):
                for stmt in true_block:
                    self.eval(stmt)
            else:
                for stmt in false_block:
                    self.eval(stmt)

        elif node_type == 'while':
            _, cond, body = node
            while self.eval(cond):
                for stmt in body:
                    self.eval(stmt)

        elif node_type == 'for':
            _, init_stmt, cond_expr, post_stmt, body = node
            self.eval(init_stmt)
            while self.eval(cond_expr):
                for stmt in body:
                    self.eval(stmt)
                self.eval(post_stmt)

        else:
            raise NotImplementedError(f"Unknown node type: {node_type}")
