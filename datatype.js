// require.config({ paths: { 'vs': 'https://cdn.jsdelivr.net/npm/monaco-editor@0.44.0/min/vs' } });
//     require(['vs/editor/editor.main'], function () {
//         function createEditor(containerId, filePath) {
//             fetch(filePath)
//             .then(response => response.text())
//             .then(code => {
//                 monaco.editor.create(document.getElementById(containerId), {
//                     value: code,
//                     language: 'python',
//                     theme: 'vs-dark',
//                     fontSize: 16,
//                     lineHeight: 24,
//                     automaticLayout: true,
//                     tabSize: 4,
//                     insertSpaces: true,
//                     padding: { top: 20 },
//                     readOnly: true,
//                     scrollbar: {
//                         vertical: 'hidden',
//                         horizontal: 'hidden',
//                         handleMouseWheel: false,
//                         alwaysConsumeMouseWheel: false
//                     },
//                     minimap: {
//                         enabled: false
//                     }
//                 });
//             });
//         }
//     createEditor('editor', 'python-lesson/template.py');
//     createEditor('list', 'python-lesson/list.py');
//     createEditor('dict', 'python-lesson/dict.py');
//     createEditor('string', 'python-lesson/string.py');
//     createEditor('tuple', 'python-lesson/tuple.py');
//     createEditor('set', 'python-lesson/set.py');
//     createEditor('frozenset', 'python-lesson/frozenset.py');
//     createEditor('math', 'python-lesson/math.py');
// });
//
