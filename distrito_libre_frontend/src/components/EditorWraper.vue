<script setup lang="ts">
import { useEditor, EditorContent } from "@tiptap/vue-3";
import type { Level } from "@tiptap/extension-heading";
import StarterKit from "@tiptap/starter-kit";
import Image from "@tiptap/extension-image";
import Placeholder from "@tiptap/extension-placeholder";
import { Icon } from "@iconify/vue";
import { useTemplateRef } from "vue";

const levels: Level[] = [1, 2, 3];

const model = defineModel<string>();

const headingsel = useTemplateRef("headingsel");

const editor = useEditor({
    extensions: [
        StarterKit.configure({
            heading: {
                levels: levels,
            },
        }),
        Image,
        Placeholder.configure({ placeholder: "Write text or Markdown! ..." }),
    ],
    content: model.value,
    onTransaction: ({ editor }) => {
        let lev = 0;
        if (editor.isActive("heading")) {
            for (lev of levels) {
                if (editor.isActive("heading", { level: lev })) break;
            }
        }
        if (headingsel.value) headingsel.value.value = lev?.toString();
    },
    onUpdate: ({ editor }) => {
        model.value = editor.getHTML();
    },
});

function onHeading() {
    if (!editor.value) return;
    if (headingsel.value?.value == "0") {
        editor.value.chain().focus().setParagraph().run();
    } else {
        editor.value
            .chain()
            .focus()
            .setHeading({ level: Number(headingsel.value?.value) as Level })
            .run();
    }
}

function onImage() {
    if (!editor.value) return;
    const url = window.prompt("Image Url");
    if (url) editor.value.chain().focus().setImage({ src: url }).run();
}
</script>

<template>
    <div v-if="editor">
        <div id="control-grp">
            <button
                :class="{ boldtxt: editor.isActive('bold') }"
                @click.prevent="editor.chain().focus().toggleBold().run()"
            >
                B
            </button>
            <button @click.prevent="onImage">
                <Icon icon="material-symbols:image-outline"></Icon>
            </button>
            <!-- TODO  -->
            <select ref="headingsel" @change="onHeading">
                <option value="0">Paragraph</option>
                <option value="1">Header 1</option>
                <option value="2">Header 2</option>
                <option value="3">Header 3</option>
            </select>
        </div>
        <EditorContent :editor="editor"></EditorContent>
    </div>
</template>

<style>
.tiptap {
    min-height: 10rem;
    border: var(--pixel-border);
    padding: 1rem;
}

.tiptap:focus {
    outline: var(--focus-outline);
}

.tiptap img {
    min-width: 0;
    max-width: 100%;
}

p.is-editor-empty:first-child::before {
    color: var(--color-gray);
    content: attr(data-placeholder);
    float: left;
    height: 0;
    pointer-events: none;
}

.boldtxt {
    font-weight: 800;
}

#control-grp {
    border: var(--pixel-border);
    padding: 0.5rem;
    margin-bottom: 0.5rem;
    display: flex;
    gap: 1rem;
}
#control-grp > button,
select {
    border: none;
    min-width: 2.5rem;
}
#control-grp > button {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
</style>
